from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from django.utils.html import mark_safe

from tags.models import Tag


class PostBaseModel(models.Model):
    title = models.CharField(max_length=200, verbose_name='название')
    text = RichTextUploadingField(verbose_name='текст')
    description_tag = models.TextField(
        max_length=200, blank=True, verbose_name='тег description', help_text='Максимальная длина 200 символов.'
    )
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(PostBaseModel):
    slug = models.SlugField(max_length=200, unique=True, verbose_name='ссылка')
    poster = models.ImageField(upload_to='', blank=True, null=True, verbose_name='постер')
    tag = models.ManyToManyField(Tag, blank=True, verbose_name='теги')
    is_published = models.BooleanField(default=False, verbose_name='пост опубликован')

    class Meta:
        ordering = ['-created']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])


class PostAbout(PostBaseModel):
    class Meta:
        verbose_name = 'О блоге'
        verbose_name_plural = 'О блоге'

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to='', verbose_name='изображение')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'изображение №{self.pk}'

    def get_image_url(self):
        return mark_safe(f'<h3>{self.image.url}</h3>')
    get_image_url.short_description = 'ссылка для вставки'

    def get_image_tag(self):
        return mark_safe(f'<img src="{self.image.url}" width="150" height="auto"/>')
    get_image_tag.short_description = 'миниатюра'
