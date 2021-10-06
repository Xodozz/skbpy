from django.db import models

from django.contrib.auth.models import User


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="Ссылка")
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts', verbose_name="Автор")
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField(verbose_name="Контент")
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    status = models.IntegerField(choices=STATUS, default=0, verbose_name="Статус")
    image = models.ImageField( blank=True, null=True, verbose_name="Превью")

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title