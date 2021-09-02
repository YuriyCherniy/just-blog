from django import forms

from captcha.fields import CaptchaField

from .models import GuestPost, GuestComment


class GuestPostForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = GuestPost
        fields = ['anonymous_username', 'text']


class GuestCommentForm(forms.ModelForm):
    guest_post_pk = forms.IntegerField(widget=forms.HiddenInput)

    class Meta:
        model = GuestComment
        fields = ['username', 'text']
