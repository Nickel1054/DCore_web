from django import template

register = template.Library()


@register.filter(is_safe=True, name='split_class')
def split_class(value: str):
    return value.replace('-', '_').split('_')[0]


