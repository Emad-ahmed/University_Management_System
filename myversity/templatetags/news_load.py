from django import template
from datetime import datetime

register = template.Library()


@register.filter(name='cutword')
def cutword(description):
    return description[:80]
