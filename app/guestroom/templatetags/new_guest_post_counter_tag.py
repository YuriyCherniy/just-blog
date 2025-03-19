from django import template

from guestroom.models import NewGuestPostCounter

register = template.Library()


@register.simple_tag
def count_new_guest_post():
    obj = NewGuestPostCounter.objects.first()
    if obj.counter > 99:
        return '99+'
    return obj.counter
