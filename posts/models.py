from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse

from tags.models import Tag


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    poster = models.ImageField(upload_to='', blank=True, null=True)
    text = RichTextUploadingField()
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    tag = models.ManyToManyField(Tag, blank=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])


class PostAbout(models.Model):
    title = models.CharField(max_length=200)
    text = RichTextUploadingField()
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
