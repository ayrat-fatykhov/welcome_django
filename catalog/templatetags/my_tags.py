from datetime import datetime

from django import template


register = template.Library()


@register.filter()
def split(text):
    return text[:100]


@register.filter()
def mymedia(val):
    if val:
        return f'/media/{val}'
    return '#'


@register.filter()
def format_date(date):
    new_format = date.strftime('%d.%m.%y %H:%M')
    return new_format
