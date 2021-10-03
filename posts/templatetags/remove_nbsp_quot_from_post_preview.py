from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()


@register.filter
@stringfilter
def remove_nbsp_quot(text):
    text.replace('&nbsp;', '')
    text.replace('&quot;', '')
    return text
