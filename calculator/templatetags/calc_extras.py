import pandas as pd
from django import template

register = template.Library()


@register.filter(is_safe=True, name='split_class')
def split_class(value: str):
    return value.replace('-', '_').split('_')[0]


@register.filter(is_safe=True, name='class_visible')
def class_visible(value: str):
    return 'select-vis' in value.__class__.__name__


@register.filter(is_safe=True, name='get_username')
def get_username(value):
    return value.username.split('@')[0]


@register.filter(is_safe=True, name='get_class')
def get_class(value: str):
    return value.__class__.__name__


@register.filter(is_safe=True, name='remove_number')
def remove_number(value: str):
    return value.rsplit('_', 1)[0]


@register.filter(is_safe=True, name='get_column_number')
def get_column_number(value: str):
    return value.rsplit('_', 1)[-1]


@register.filter(is_safe=True, name='get_sell')
def get_sell(value: pd.DataFrame):
    return [col for col in value.columns if 'SELL' in col][0].replace('SELL', '')


@register.filter(is_safe=True, name='get_buy')
def get_buy(value: pd.DataFrame):
    return [col for col in value.columns if 'SELL' in col][0].replace('SELL', '')


if __name__ == '__main__':
    get_sell(pd.DataFrame({'column_BUY': [0, 1, 2, 5], 'column2_SELL': [5, 6, 97, 8]}))