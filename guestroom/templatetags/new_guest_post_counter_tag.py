from django import template

from guestroom.models import NewGuestPostCounterModel

register = template.Library()


@register.simple_tag
def count_new_guest_post():
    obj = NewGuestPostCounterModel.objects.first()
    if obj.counter > 99:
        return '99+'
    return obj.counter
