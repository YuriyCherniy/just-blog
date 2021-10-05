from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()


@register.filter
@stringfilter
def remove_special_char(text):
    text = text.replace('&#39;', '')  # remove single quot char
    text = text.replace('&quot;', '')  # remove double quot char
    return text
