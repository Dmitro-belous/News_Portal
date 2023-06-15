from django.core.management.base import BaseCommand, CommandError
from news_site.models import Post, Category


class Command(BaseCommand):
    help = 'Удаляет все новости выбранной категории'  # показывает подсказку при вводе "python manage.py <ваша команда> --help"
    requires_migrations_checks = True  # напоминать ли о миграциях. Если тру — то будет напоминание о том, что не сделаны все миграции (если такие есть)

    def handle(self, *args, **options):
        # здесь можете писать любой код, который выполняется при вызове вашей команды
        self.stdout.readable()
        self.stdout.write(
            'Введите категорию:')
        category_answer = input()
        for category in Category.objects.all():
            if category_answer == category.name:
                self.stdout.write(
                    'Вы действительно хотите удалить эти посты? да/нет')  # спрашиваем пользователя действительно ли он хочет удалить все товары
                answer = input()  # считываем подтверждение

                if answer == 'да':  # в случае подтверждения действительно удаляем все товары
                    Post.objects.filter(category=category).delete()
                    self.stdout.write(self.style.SUCCESS('Посты успешно удалены!'))
                    return

        self.stdout.write(
        self.style.ERROR('В доступе отказано'))  # в случае неправильного подтверждения, говорим что в доступе отказано