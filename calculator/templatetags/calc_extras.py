from django import template

register = template.Library()


@register.filter(is_safe=True, name='get_class')
def get_class(value):
    return value.__class__.__name__
