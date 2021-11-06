from django.db import models

from django.contrib.auth.models import User


STATUS = (
    (0,"Черновик"),
    (1,"Публикация")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="Ссылка")
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts', verbose_name="Автор")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(verbose_name="Контент")
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    status = models.IntegerField(choices=STATUS, default=0, verbose_name="Статус")
    image = models.ImageField(blank=True, null=True, verbose_name="Превью поста")

    class Meta:
        ordering = ['-created_on']

    def image_img(self):
        if self.image:
            from django.utils.safestring import mark_safe
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.image.url))
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True

    def __str__(self):
        return self.title


class Banner(models.Model):
    # title = models.CharField(max_length=200, unique=True, verbose_name="Название")

    images = models.ImageField(blank=True, null=True, verbose_name="Картинка")


    def image_img(self):
        if self.images:
            from django.utils.safestring import mark_safe
            return mark_safe(u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.images.url))
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True

