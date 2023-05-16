from django import forms
from .dict_data.form_values import COMMODITIES, EXCHANGE, HUBS, DAM_ZONES, FUTURES, CO2, LOAD_TYPES, PRODUCT_TYPES, \
    DELIVERY_PERIOD


class DateInput(forms.DateInput):
    input_type = 'date'
    format = '%d/%m/%Y'


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
                                        widget=forms.Select(attrs={'onchange': 'zone_change(this.id)'}))
    zone_icis_gas_2 = forms.ChoiceField(label='Zone 2', choices=HUBS['icis'], initial='empty',
                                        widget=forms.Select(attrs={'onchange': 'zone_change(this.id)'}))

    zone_eex_gas_1 = forms.ChoiceField(label='Zone 1', choices=HUBS['eex'], initial='empty',
                                       widget=forms.Select(attrs={'onchange': 'zone_change(this.id)'}))
    zone_eex_gas_2 = forms.ChoiceField(label='Zone 2', choices=HUBS['eex'], initial='empty',
                                       widget=forms.Select(attrs={'onchange': 'zone_change(this.id)'}))

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
                                   widget=forms.Select(attrs={'onchange': 'zone_change(this.id)'}))
    zone_co2_2 = forms.ChoiceField(label='CO2 Zones 2', choices=CO2['eex'], initial='empty',
                                   widget=forms.Select(attrs={'onchange': 'zone_change(this.id)'}))

    ###

    load_type_1 = forms.ChoiceField(label='Load type 1', choices=LOAD_TYPES, initial='empty',
                                    widget=forms.Select(attrs={'onchange': ''}))
    load_type_2 = forms.ChoiceField(label='Load type 1', choices=LOAD_TYPES, initial='empty',
                                    widget=forms.Select(attrs={'onchange': ''}))

    ###

    product_types_eex_1 = forms.ChoiceField(label='Product type 1', choices=PRODUCT_TYPES['eex'], initial='empty',
                                            widget=forms.Select(attrs={'onchange': 'product_change(this.id)'}))
    product_types_eex_2 = forms.ChoiceField(label='Product type 2', choices=PRODUCT_TYPES['eex'], initial='empty',
                                            widget=forms.Select(attrs={'onchange': 'product_change(this.id)'}))

    product_types_icis_1 = forms.ChoiceField(label='Product type 1', choices=PRODUCT_TYPES['icis'], initial='empty',
                                             widget=forms.Select(attrs={'onchange': 'product_change(this.id)'}))
    product_types_icis_2 = forms.ChoiceField(label='Product type 2', choices=PRODUCT_TYPES['icis'], initial='empty',
                                             widget=forms.Select(attrs={'onchange': 'product_change(this.id)'}))

    product_types_tge_1 = forms.ChoiceField(label='Product type 1', choices=PRODUCT_TYPES['tge'], initial='empty',
                                            widget=forms.Select(attrs={'onchange': 'product_change(this.id)'}))
    product_types_tge_2 = forms.ChoiceField(label='Product type 2', choices=PRODUCT_TYPES['tge'], initial='empty',
                                            widget=forms.Select(attrs={'onchange': 'product_change(this.id)'}))

    product_types_spot_1 = forms.ChoiceField(label='Product type 1', choices=PRODUCT_TYPES['spot'], initial='empty',
                                             widget=forms.Select(attrs={'onchange': 'product_change(this.id)'}))
    product_types_spot_2 = forms.ChoiceField(label='Product type 2', choices=PRODUCT_TYPES['spot'], initial='empty',
                                             widget=forms.Select(attrs={'onchange': 'product_change(this.id)'}))

    product_types_co2_1 = forms.ChoiceField(label='Product type 1', choices=PRODUCT_TYPES['spot'], initial='empty',
                                            widget=forms.Select(attrs={'onchange': 'product_change(this.id)'}))
    product_types_co2_2 = forms.ChoiceField(label='Product type 2', choices=PRODUCT_TYPES['spot'], initial='empty',
                                            widget=forms.Select(attrs={'onchange': 'product_change(this.id)'}))

    ### DELIVERY PERIOD

    period_date_field_1 = forms.DateField(label='Delivery Period Day 1', widget=DateInput())
    period_date_field_2 = forms.DateField(label='Delivery Period Day 2', widget=DateInput())

    period_week_1 = forms.ChoiceField(label='Week 1', choices=DELIVERY_PERIOD['week'], initial='empty',
                                      widget=forms.Select(attrs={'onchange': 'delivery_period_change(this.id)'}))
    period_week_2 = forms.ChoiceField(label='Week 2', choices=DELIVERY_PERIOD['week'], initial='empty',
                                      widget=forms.Select(attrs={'onchange': 'delivery_period_change(this.id)'}))

    period_weekend_1 = forms.ChoiceField(label='Weekend 1', choices=DELIVERY_PERIOD['weekend'], initial='empty',
                                         widget=forms.Select(attrs={'onchange': 'delivery_period_change(this.id)'}))
    period_weekend_2 = forms.ChoiceField(label='Weekend 2', choices=DELIVERY_PERIOD['weekend'], initial='empty',
                                         widget=forms.Select(attrs={'onchange': 'delivery_period_change(this.id)'}))

    period_month_1 = forms.ChoiceField(label='Month 1', choices=DELIVERY_PERIOD['month'], initial='empty',
                                       widget=forms.Select(attrs={'onchange': 'delivery_period_change(this.id)'}))
    period_month_2 = forms.ChoiceField(label='Month 2', choices=DELIVERY_PERIOD['month'], initial='empty',
                                       widget=forms.Select(attrs={'onchange': 'delivery_period_change(this.id)'}))

    period_quarter_1 = forms.ChoiceField(label='Quarter 1', choices=DELIVERY_PERIOD['quarter'], initial='empty',
                                         widget=forms.Select(attrs={'onchange': 'delivery_period_change(this.id)'}))
    period_quarter_2 = forms.ChoiceField(label='Quarter 2', choices=DELIVERY_PERIOD['quarter'], initial='empty',
                                         widget=forms.Select(attrs={'onchange': 'delivery_period_change(this.id)'}))

    period_season_1 = forms.ChoiceField(label='Season 1', choices=DELIVERY_PERIOD['season'], initial='empty',
                                        widget=forms.Select(attrs={'onchange': 'delivery_period_change(this.id)'}))
    period_season_2 = forms.ChoiceField(label='Season 2', choices=DELIVERY_PERIOD['season'], initial='empty',
                                        widget=forms.Select(attrs={'onchange': 'delivery_period_change(this.id)'}))

    period_year_1 = forms.ChoiceField(label='Year 1', choices=DELIVERY_PERIOD['year'], initial='empty',
                                      widget=forms.Select(attrs={'onchange': 'delivery_period_change(this.id)'}))
    period_year_2 = forms.ChoiceField(label='Year 2', choices=DELIVERY_PERIOD['year'], initial='empty',
                                      widget=forms.Select(attrs={'onchange': 'delivery_period_change(this.id)'}))

    period_gas_year_1 = forms.ChoiceField(label='Gas Year 1', choices=DELIVERY_PERIOD['gas_year'], initial='empty',
                                          widget=forms.Select(attrs={'onchange': 'delivery_period_change(this.id)'}))
    period_gas_year_2 = forms.ChoiceField(label='Gas Year 2', choices=DELIVERY_PERIOD['gas_year'], initial='empty',
                                          widget=forms.Select(attrs={'onchange': 'delivery_period_change(this.id)'}))

    year_1 = forms.ChoiceField(label='Delivery Year 1', choices=DELIVERY_PERIOD['year'], initial='empty',
                               widget=forms.Select(attrs={'onchange': ''}))
    year_2 = forms.ChoiceField(label='Delivery Year 2', choices=DELIVERY_PERIOD['year'], initial='empty',
                               widget=forms.Select(attrs={'onchange': ''}))

    period_deliverystart_1 = forms.DateField(label='Delivery Start 1', widget=DateInput())
    period_deliverystart_2 = forms.DateField(label='Delivery Start 2', widget=DateInput())

    period_deliveryend_1 = forms.DateField(label='Delivery End 1', widget=DateInput())
    period_deliveryend_2 = forms.DateField(label='Delivery End 2', widget=DateInput())
