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
    return '/media/blog/Blog-intro.jpg'
