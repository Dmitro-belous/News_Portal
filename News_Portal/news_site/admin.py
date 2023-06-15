from django.contrib import admin
from .models import Post, Category, Author, PostAdmin


# создаём новый класс для представления товаров в админке
class PostAdminList(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    list_display = [field.name for field in Post._meta.get_fields()] # генерируем список имён всех полей для более красивого отображения


admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Post, PostAdmin)
