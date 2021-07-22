from django.db import models
from django.urls import reverse


class GuestPost(models.Model):
    anonymous_username = models.CharField(max_length=40, verbose_name='Представьтесь:')
    text = models.TextField(max_length=700, verbose_name='Текст:')
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.anonymous_username

    def get_absolute_url(self):
        return reverse('guest_post_update', args=[self.pk])


class GuestComment(models.Model):
    username = models.CharField(max_length=40, verbose_name='Имя администратора:')
    text = models.TextField(max_length=700, verbose_name='Текст:')
    guest_post = models.OneToOneField(GuestPost, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text[:40]

    def get_absolute_url(self):
        return reverse('guest_comment_update', args=[self.pk])
