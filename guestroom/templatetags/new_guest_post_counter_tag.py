from django import template

from guestroom.services import NewGuestPostCounter

register = template.Library()
post_counter = NewGuestPostCounter()


@register.simple_tag
def count_new_guest_post():
    result = post_counter.get_counter()
    if result > 99:
        return '99+'
    return result
