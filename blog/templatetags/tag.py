from django import template

register = template.Library()

@register.simple_tag
def getDateMonth(month):
    return "Jun"