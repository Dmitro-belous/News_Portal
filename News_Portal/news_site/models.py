from django.contrib.admin import TabularInline, ModelAdmin
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    author_rating = models.SmallIntegerField(default=0)

    def update_rating(self):
        post_rat = self.post_set.aggregate(post_rating=Sum('rating'))
        p_rat = 0
        p_rat += post_rat.get('post_rating')

        comment_rat = self.user.comment_set.aggregate(comment_rating=Sum('rating'))
        c_rat = 0
        c_rat += comment_rat.get('comment_rating')

        self.author_rating = p_rat * 3 + c_rat
        self.save()

    def __str__(self):
        return f'{self.user}'


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHOICES = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья')
    )
    categoryType = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=ARTICLE)
    time_add = models.DateTimeField(auto_now_add=True)
    head = models.CharField(max_length=256)
    body = models.TextField()
    rating = models.SmallIntegerField(default=0)
    category = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return f'{self.body[:123]}...'

    def __str__(self):
        return f'{self.head}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    comment_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    time_add = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


# наследуемся от класса TabularInline
class CategoryInline(TabularInline):
    # указываем в качестве модели промежуточный класс
    model = PostCategory
    extra = 1


# Новый (дополнительный к Post) класс использует CategoryInline в качестве
# инлайн-класса для отображения ManyToMany поля
class PostAdmin(ModelAdmin):
    inlines = (CategoryInline,)
