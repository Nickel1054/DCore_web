from django import forms
from dynamic_forms import DynamicField, DynamicFormMixin


class CalculatorForm(DynamicFormMixin, forms.Form):
    COMMODITIES = [
        ('empty', '--'),
        ('gas', 'Gas'),
        ('clean_spark', 'Clean spark spread'),
        ('spark', 'Spark spread'),
        ('electricity_spot', 'Electricity spot'),
        ('electricity_futures', 'Electricity futures'),
        ('co2', 'CO2'),
    ]

    commodity = forms.CharField(label='Commodity', widget=forms.Select(choices=COMMODITIES, attrs={
        'onchange': 'dynamic_form()'}), initial='empty',)
    # exchange = DynamicField(forms.ChoiceField,
    #                         choices=lambda form: form.EXCHANGE[form["commodity"].value()],)
