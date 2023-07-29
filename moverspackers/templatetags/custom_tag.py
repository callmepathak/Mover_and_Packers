from django import template
from moverspackers.models import *
register = template.Library()

@register.filter(name = 'notification')
def notification(obj):
    booking  = SiteUser.objects.filter(status=None)
    return booking

@register.simple_tag()
def notificationcount(*args, **kwargs):
    bookingcount  = SiteUser.objects.filter(status=None).count()
    return bookingcount