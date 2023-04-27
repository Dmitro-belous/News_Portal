from datetime import timedelta
import logging

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.mail import EmailMultiAlternatives
from django.core.management.base import BaseCommand
from django.template.loader import render_to_string
from django.utils import timezone
from django_apscheduler import util
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution

from news_site.models import Post, Category

logger = logging.getLogger(__name__)


def my_job():

    for category in Category.objects.all():

        mailing_list = list(
            category.subscribers.all(
            ).values_list(
                'username',
                'first_name',
                'email',
                'categories'
            )
        )

        posts_list = list(
            category.post_set.filter(
                time_add__gt=timezone.now() - timedelta(days=7)
            ))

        if len(mailing_list) > 0 and len(posts_list) > 0:
            for user, first_name, email, category_name in mailing_list:
                if not first_name:
                    first_name = user

                html_content = render_to_string(
                    'weekly_post.html',
                    {
                        'name': first_name,
                        'category': category,
                        'posts': posts_list,
                        'link': settings.SITE_URL
                    }
                )

                message = EmailMultiAlternatives(
                    subject=f'Все посты за последнюю неделю в категории"{category}"',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[email]

                )
                message.attach_alternative(html_content, 'text/html')
                message.send()


# The `close_old_connections` decorator ensures that database connections,
# that have become unusable or are obsolete, are closed before and after your
# job has run. You should use it to wrap any jobs that you schedule that access
# the Django database in any way.
@util.close_old_connections
def delete_old_job_executions(max_age=604_800):
    """
    This job deletes APScheduler job execution entries older than `max_age`
    from the database.
    It helps to prevent the database from filling up with old historical
    records that are no longer useful.

    :param max_age: The maximum length of time to retain historical
                    job execution records. Defaults to 7 days.
    """
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        scheduler.add_job(
            my_job,
            trigger=CronTrigger(day_of_week='fri', hour='18', minute='0'),
            id="my_job",  # The `id` assigned to each job MUST be unique
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'my_job'.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added weekly job: 'delete_old_job_executions'.")

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")
