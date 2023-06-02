from django import template

register = template.Library()


@register.filter(is_safe=True, name='split_class')
def split_class(value: str):
    return value.replace('-', '_').split('_')[0]


@register.filter(is_safe=True, name='class_visible')
def class_visible(value: str):
    return 'select-vis' in value.__class__.__name__


@register.filter(is_safe=True, name='get_class')
def get_class(value: str):
    return value.__class__.__name__


@register.filter(is_safe=True, name='remove_number')
def remove_number(value: str):
    return value.rsplit('_', 1)[0]


@register.filter(is_safe=True, name='get_column_number')
def get_column_number(value: str):
    return value.rsplit('_', 1)[-1]
