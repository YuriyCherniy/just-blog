from django.db import models
from tinymce.models import HTMLField
from django.urls import reverse

from tags.models import Tag


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    text = HTMLField()
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    tag = models.ManyToManyField(Tag, blank=True)

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
