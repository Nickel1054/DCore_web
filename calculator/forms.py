from django import forms
from .dict_data.form_values import COMMODITIES, EXCHANGE, HUBS, DAM_ZONES, FUTURES, CO2, LOAD_TYPES


class CalculatorForm(forms.Form):
    commodity = forms.ChoiceField(
        label='Commodity',
        widget=forms.Select(attrs={'class': 'select-vis', 'onchange': 'commodity_change()'}),
        choices=COMMODITIES,
        initial='empty')

    ##########

    exchange_gas_1 = forms.ChoiceField(label='Gas Source 1', choices=EXCHANGE['gas'], initial='empty',
                                       widget=forms.Select(attrs={'onchange': 'gas_source_change(this.id)'}))
    exchange_gas_2 = forms.ChoiceField(label='Gas Source 2', choices=EXCHANGE['gas'], initial='empty',
                                       widget=forms.Select(attrs={'onchange': 'gas_source_change(this.id)'}))

    exchange_ee_spot_1 = forms.ChoiceField(label='DAM 1', choices=EXCHANGE['electricity_spot'], initial='empty',
                                           widget=forms.Select(attrs={'onchange': 'ee_spot_source_change(this.id)'}))
    exchange_ee_spot_2 = forms.ChoiceField(label='DAM 2', choices=EXCHANGE['electricity_spot'], initial='empty',
                                           widget=forms.Select(attrs={'onchange': 'ee_spot_source_change(this.id)'}))

    exchange_ee_futures_1 = forms.ChoiceField(label='EE Futures 1', choices=EXCHANGE['electricity_futures'],
                                              initial='empty',
                                              widget=forms.Select(
                                                  attrs={'onchange': 'ee_futures_source_change(this.id)'}))
    exchange_ee_futures_2 = forms.ChoiceField(label='EE Futures 2', choices=EXCHANGE['electricity_futures'],
                                              initial='empty',
                                              widget=forms.Select(
                                                  attrs={'onchange': 'ee_futures_source_change(this.id)'}))
    exchange_co2_1 = forms.ChoiceField(label='CO2 1', choices=EXCHANGE['co2'], initial='empty',
                                       widget=forms.Select(attrs={'onchange': 'co2_source_change(this.id)'}))
    exchange_co2_2 = forms.ChoiceField(label='CO2 2', choices=EXCHANGE['co2'], initial='empty',
                                       widget=forms.Select(attrs={'onchange': 'co2_source_change(this.id)'}))

    ##########

    zone_icis_gas_1 = forms.ChoiceField(label='Zone 1', choices=HUBS['icis'], initial='empty',
                                        widget=forms.Select(attrs={'onchange': 'button_change()'}))
    zone_icis_gas_2 = forms.ChoiceField(label='Zone 2', choices=HUBS['icis'], initial='empty',
                                        widget=forms.Select(attrs={'onchange': 'button_change()'}))

    zone_eex_gas_1 = forms.ChoiceField(label='Zone 1', choices=HUBS['eex'], initial='empty',
                                       widget=forms.Select(attrs={'onchange': 'button_change()'}))
    zone_eex_gas_2 = forms.ChoiceField(label='Zone 2', choices=HUBS['eex'], initial='empty',
                                       widget=forms.Select(attrs={'onchange': 'button_change()'}))

    zone_ee_spot_1 = forms.ChoiceField(label='Spot zone 1', choices=DAM_ZONES['electricity_spot'], initial='empty',
                                       widget=forms.Select(attrs={'onchange': 'zone_change(this.id)'}))
    zone_ee_spot_2 = forms.ChoiceField(label='Spot zone 2', choices=DAM_ZONES['electricity_spot'], initial='empty',
                                       widget=forms.Select(attrs={'onchange': 'zone_change(this.id)'}))

    zone_ee_futures_tge_1 = forms.ChoiceField(label='Futures Zone 1', choices=FUTURES['tge'], initial='empty',
                                              widget=forms.Select(attrs={'onchange': 'zone_change(this.id)'}))
    zone_ee_futures_tge_2 = forms.ChoiceField(label='Futures Zone 2', choices=FUTURES['tge'], initial='empty',
                                              widget=forms.Select(attrs={'onchange': 'zone_change(this.id)'}))
    zone_ee_futures_eex_1 = forms.ChoiceField(label='Futures Zone 1', choices=FUTURES['eex'], initial='empty',
                                              widget=forms.Select(attrs={'onchange': 'zone_change(this.id)'}))
    zone_ee_futures_eex_2 = forms.ChoiceField(label='Futures Zone 2', choices=FUTURES['eex'], initial='empty',
                                              widget=forms.Select(attrs={'onchange': 'zone_change(this.id)'}))

    zone_co2_1 = forms.ChoiceField(label='CO2 Zones 1', choices=CO2['eex'], initial='empty',
                                   widget=forms.Select(attrs={'onchange': 'button_change()'}))
    zone_co2_2 = forms.ChoiceField(label='CO2 Zones 2', choices=CO2['eex'], initial='empty',
                                   widget=forms.Select(attrs={'onchange': 'button_change()'}))

    ###

    load_type_1 = forms.ChoiceField(label='Load type 1', choices=LOAD_TYPES, initial='empty',
                                    widget=forms.Select(attrs={'onchange': 'zone_change'}))
    load_type_2 = forms.ChoiceField(label='Load type 1', choices=LOAD_TYPES, initial='empty',
                                    widget=forms.Select(attrs={'onchange': 'zone_change'}))
