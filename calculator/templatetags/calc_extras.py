from django import template

register = template.Library()


@register.filter(is_safe=True, name='split_class')
def split_class(value: str):
    return value.replace('-', '_').split('_')[0]


@register.filter(is_safe=True, name='remove_number')
def split_class(value: str):
    return value.rsplit('_', 1)[0]


@register.filter(is_safe=True, name='get_column_number')
def get_column_number(value: str):
    return value.rsplit('_', 1)[-1]
