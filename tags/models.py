from django.db import models
from django.urls import reverse


class Tag(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_from_tag', args=[self.slug])
