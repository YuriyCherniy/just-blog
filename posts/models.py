from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from django.utils.html import mark_safe

from tags.models import Tag


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='название')
    slug = models.SlugField(max_length=200, unique=True, verbose_name='ссылка')
    poster = models.ImageField(upload_to='', blank=True, null=True, verbose_name='постер')
    text = RichTextUploadingField(verbose_name='текст')
    tag = models.ManyToManyField(Tag, blank=True, verbose_name='теги')
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='', blank=True, null=True, verbose_name='изображение')
    image_1 = models.ImageField(upload_to='', blank=True, null=True, verbose_name='изображение')
    image_2 = models.ImageField(upload_to='', blank=True, null=True, verbose_name='изображение')
    image_3 = models.ImageField(upload_to='', blank=True, null=True, verbose_name='изображение')
    image_4 = models.ImageField(upload_to='', blank=True, null=True, verbose_name='изображение')
    image_5 = models.ImageField(upload_to='', blank=True, null=True, verbose_name='изображение')
    image_6 = models.ImageField(upload_to='', blank=True, null=True, verbose_name='изображение')
    image_7 = models.ImageField(upload_to='', blank=True, null=True, verbose_name='изображение')
    image_8 = models.ImageField(upload_to='', blank=True, null=True, verbose_name='изображение')
    image_9 = models.ImageField(upload_to='', blank=True, null=True, verbose_name='изображение')

    class Meta:
        ordering = ['-created']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])

    def get_image_url(self):
        return mark_safe(f'<h3>{self.image.url}</h3>')
    get_image_url.short_description = 'ссылка для вставки'

    def get_image(self):
        return mark_safe(f'<img src="{self.image.url}" width="150" height="auto"/>')
    get_image.short_description = 'миниатюра'

    def get_image_url_1(self):
        return mark_safe(f'<h3>{self.image_1.url}</h3>')
    get_image_url_1.short_description = 'ссылка для вставки'

    def get_image_1(self):
        return mark_safe(f'<img src="{self.image_1.url}" width="150" height="auto"/>')
    get_image_1.short_description = 'миниатюра'

    def get_image_url_2(self):
        return mark_safe(f'<h3>{self.image_2.url}</h3>')
    get_image_url_2.short_description = 'ссылка для вставки'

    def get_image_2(self):
        return mark_safe(f'<img src="{self.image_2.url}" width="150" height="auto"/>')
    get_image_2.short_description = 'миниатюра'

    def get_image_url_3(self):
        return mark_safe(f'<h3>{self.image_3.url}</h3>')
    get_image_url_3.short_description = 'ссылка для вставки'

    def get_image_3(self):
        return mark_safe(f'<img src="{self.image_3.url}" width="150" height="auto"/>')
    get_image_3.short_description = 'миниатюра'

    def get_image_url_4(self):
        return mark_safe(f'<h3>{self.image_4.url}</h3>')
    get_image_url_4.short_description = 'ссылка для вставки'

    def get_image_4(self):
        return mark_safe(f'<img src="{self.image_4.url}" width="150" height="auto"/>')
    get_image_4.short_description = 'миниатюра'

    def get_image_url_5(self):
        return mark_safe(f'<h3>{self.image_5.url}</h3>')
    get_image_url_5.short_description = 'ссылка для вставки'

    def get_image_5(self):
        return mark_safe(f'<img src="{self.image_5.url}" width="150" height="auto"/>')
    get_image_5.short_description = 'миниатюра'

    def get_image_url_6(self):
        return mark_safe(f'<h3>{self.image_6.url}</h3>')
    get_image_url_6.short_description = 'ссылка для вставки'

    def get_image_6(self):
        return mark_safe(f'<img src="{self.image_6.url}" width="150" height="auto"/>')
    get_image_6.short_description = 'миниатюра'

    def get_image_url_7(self):
        return mark_safe(f'<h3>{self.image_7.url}</h3>')
    get_image_url_7.short_description = 'ссылка для вставки'

    def get_image_7(self):
        return mark_safe(f'<img src="{self.image_7.url}" width="150" height="auto"/>')
    get_image_7.short_description = 'миниатюра'

    def get_image_url_8(self):
        return mark_safe(f'<h3>{self.image_8.url}</h3>')
    get_image_url_8.short_description = 'ссылка для вставки'

    def get_image_8(self):
        return mark_safe(f'<img src="{self.image_8.url}" width="150" height="auto"/>')
    get_image_8.short_description = 'миниатюра'

    def get_image_url_9(self):
        return mark_safe(f'<h3>{self.image_9.url}</h3>')
    get_image_url_9.short_description = 'ссылка для вставки'

    def get_image_9(self):
        return mark_safe(f'<img src="{self.image_9.url}" width="150" height="auto"/>')
    get_image_9.short_description = 'миниатюра'


class PostAbout(models.Model):
    title = models.CharField(max_length=200, verbose_name='название')
    text = RichTextUploadingField(verbose_name='текст')
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'О блоге'
        verbose_name_plural = 'О блоге'

    def __str__(self):
        return self.title
