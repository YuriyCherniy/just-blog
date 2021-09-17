from django.db import models
from django.urls import reverse


class Tag(models.Model):
    title = models.CharField(max_length=20, verbose_name='Название')
    slug = models.SlugField(max_length=20, unique=True, verbose_name='Ссылка')

    class Meta:
        ordering = ['title']
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_from_tag', args=[self.slug])
