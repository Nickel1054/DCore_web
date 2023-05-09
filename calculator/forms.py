from django import forms
from .dict_data.form_values import COMMODITIES, EXCHANGE, HUBS, DAM_ZONES, FUTURES, CO2


class CalculatorForm(forms.Form):
    commodity = forms.ChoiceField(
        label='Commodity',
        widget=forms.Select(attrs={'class': 'select-vis', 'onchange': 'commodity_change()'}),
        choices=COMMODITIES,
        initial='empty')

    ##########

    exchange_gas = forms.ChoiceField(label='Gas Source', choices=EXCHANGE['gas'], initial='empty',
                                     widget=forms.Select(attrs={'onchange': 'gas_source_change()'}))
    exchange_ee_spot = forms.ChoiceField(label='DAM', choices=EXCHANGE['electricity_spot'], initial='empty',
                                         widget=forms.Select(attrs={'onchange': 'ee_spot_source_change()'}))
    exchange_ee_futures = forms.ChoiceField(label='EE Futures', choices=EXCHANGE['electricity_futures'],
                                            initial='empty',
                                            widget=forms.Select(attrs={'onchange': 'ee_futures_source_change()'}))
    exchange_co2 = forms.ChoiceField(label='CO2', choices=EXCHANGE['co2'], initial='empty',
                                     widget=forms.Select(attrs={'onchange': 'co2_source_change()'}))

    ##########

    zone_icis_gas = forms.ChoiceField(label='Zone', choices=HUBS['icis'], initial='empty',
                                      widget=forms.Select(attrs={'onchange': 'button_change()'}))
    zone_eex_gas = forms.ChoiceField(label='Zone', choices=HUBS['eex'], initial='empty',
                                     widget=forms.Select(attrs={'onchange': 'button_change()'}))

    zone_ee_spot = forms.ChoiceField(label='Spot zone', choices=DAM_ZONES['electricity_spot'], initial='empty',
                                     widget=forms.Select(attrs={'onchange': 'button_change()'}))

    zone_ee_futures_tge = forms.ChoiceField(label='Futures Zone', choices=FUTURES['tge'], initial='empty',
                                            widget=forms.Select(attrs={'onchange': 'button_change()'}))
    zone_ee_futures_eex = forms.ChoiceField(label='Futures Zone', choices=FUTURES['eex'], initial='empty',
                                            widget=forms.Select(attrs={'onchange': 'button_change()'}))

    zone_co2 = forms.ChoiceField(label='CO2 Zones', choices=CO2['eex'], initial='empty',
                                 widget=forms.Select(attrs={'onchange': 'button_change()'}))
