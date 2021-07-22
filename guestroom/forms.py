from django import forms

from .models import GuestComment


class GuestCommentForm(forms.ModelForm):
    guest_post_pk = forms.IntegerField(widget=forms.HiddenInput)

    class Meta:
        model = GuestComment
        fields = ['username', 'text']
