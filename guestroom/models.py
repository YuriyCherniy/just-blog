from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe


help_text = mark_safe(
    'This site is protected by reCAPTCHA and the Google \
    <a href="https://policies.google.com/privacy">Privacy Policy</a> and \
    <a href="https://policies.google.com/terms">Terms of Service</a> apply.'
)


class GuestPost(models.Model):
    anonymous_username = models.CharField(max_length=40, verbose_name='Представьтесь:')
    text = models.TextField(max_length=700, verbose_name='Текст:', help_text=help_text)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        verbose_name = 'гостевое сообщение'
        verbose_name_plural = 'гостевые сообщения'

    def __str__(self):
        return self.anonymous_username

    def get_absolute_url(self):
        return reverse('guest_post_detail', args=[self.pk])


class GuestComment(models.Model):
    username = models.CharField(max_length=40, default='@YuriyCherniy', verbose_name='Имя администратора:')
    text = models.TextField(max_length=700, verbose_name='Текст:')
    guest_post = models.OneToOneField(GuestPost, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии к сообщениям'

    def __str__(self):
        return self.text[:40]
