from datetime import timedelta

from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from news_site.models import Category
from django.utils import timezone


@shared_task
def send_notifications(preview, pk, title, subscribers):
    text = f'Здравствуйте! Новый пост в вашем любимом разделе!\n {preview}\nСсылка на статью: {settings.SITE_URL}/news/{pk}'
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': preview,
            'link': f'{settings.SITE_URL}/news/{pk}'
        }
    )

    msg = EmailMultiAlternatives(
        subject=title,
        body=text,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@shared_task
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
