from django import forms
from snowpenguin.django.recaptcha3.fields import ReCaptchaField

from .models import GuestComment, GuestPost


class GuestPostForm(forms.ModelForm):
    captcha = ReCaptchaField()

    class Meta:
        model = GuestPost
        fields = ['anonymous_username', 'text']


class GuestCommentForm(forms.ModelForm):
    guest_post_pk = forms.IntegerField(widget=forms.HiddenInput)

    class Meta:
        model = GuestComment
        fields = ['username', 'text']
