from django import forms
from .dict_data.form_values import EXCHANGE


class CalculatorForm(forms.Form):
    COMMODITIES = [
        ('empty', '--'),
        ('gas', 'Gas'),
        # ('clean_spark', 'Clean spark spread'),
        # ('spark', 'Spark spread'),
        ('electricity_spot', 'Electricity spot'),
        ('electricity_futures', 'Electricity futures'),
        ('co2', 'CO2'),
    ]

    commodity = forms.ChoiceField(
        label='Commodities',
        widget=forms.Select(attrs={'class': 'select-vis', 'onchange': 'commodity_change()'}),
        choices=COMMODITIES,
        initial='empty')

    exchange_gas = forms.ChoiceField(label='Gas Source', choices=EXCHANGE['gas'], initial='empty', )
    exchange_ee_spot = forms.ChoiceField(label='DAM', choices=EXCHANGE['electricity_spot'], initial='empty', )
    exchange_ee_futures = forms.ChoiceField(label='EE Futures', choices=EXCHANGE['electricity_futures'],
                                            initial='empty', )
    exchange_co2 = forms.ChoiceField(label='CO2', choices=EXCHANGE['co2'], initial='empty', )
    # exchange = DynamicField(forms.ChoiceField,
    #                         choices=lambda form: form.EXCHANGE[form["commodity"].value()],)
