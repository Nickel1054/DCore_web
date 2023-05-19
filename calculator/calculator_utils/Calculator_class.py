from ..dict_data.form_values import *


def get_dict_value(search_list, searched_value):
    for index, value in enumerate(search_list):
        if value[0] == searched_value:
            return value[1]


class Calculator:
    def __init__(self, form):
        self.a = 15
        self.form_1 = None
        self.form_2 = None
        self.clean_form(form)
        print(self.a)

    def clean_form(self, in_form):
        out_form_1 = {}
        out_form_2 = {}
        for key, value in in_form.items():
            if value != 'empty' and value != '' and value is not None:
                if key == 'commodity':
                    out_form_1[key] = value
                    out_form_2[key] = value
                if key.endswith('_1'):
                    out_form_1[key[:-2]] = value
                elif key.endswith('_2'):
                    out_form_2[key[:-2]] = value
        self.form_1 = out_form_1
        self.form_2 = out_form_2

    def get_icis(self, form_values):
        hub = get_dict_value(HUBS['icis'], form_values['zone_icis_gas'])
        q = "select trading_date, price_mid " \
            "from bi.icis_bi " \
            "left join bi.gas_icis_product gip on gip.prod_id = icis_bi.prod_id " \
            "left join bi.gas_icis_hub on gip.h_id = gas_icis_hub.h_id " \
            f"where h_name = {HUBS['icis']} and product_type = 'Day' and delivery_start_date >= '2023-01-20' " \
            "and delivery_start_date <= '2023-02-28' order by trading_date;"



        return 0

    def get_eex_gas(self):
        pass

    def get_data_for_form(self, form_data):
        if form_data['commodity'] == 'gas':
            if form_data['exchange_gas'] == 'icis':
                self.get_icis(form_data)

    def run(self):
        for form_values in [self.form_1, self.form_2]:
            self.get_data_for_form(form_values)
        return 0



if __name__ == '__main__':
    form = {'commodity': 'gas', 'exchange_gas_1': 'icis', 'exchange_gas_2': 'eex', 'exchange_ee_spot_1': 'empty',
            'exchange_ee_spot_2': 'empty', 'exchange_ee_futures_1': 'empty', 'exchange_ee_futures_2': 'empty',
            'exchange_co2_1': 'empty', 'exchange_co2_2': 'empty', 'zone_icis_gas_1': 'at', 'zone_icis_gas_2': 'empty',
            'zone_eex_gas_1': 'empty', 'zone_eex_gas_2': 'cegh', 'zone_ee_spot_1': 'empty', 'zone_ee_spot_2': 'empty',
            'zone_ee_futures_tge_1': 'empty', 'zone_ee_futures_tge_2': 'empty', 'zone_ee_futures_eex_1': 'empty',
            'zone_ee_futures_eex_2': 'empty', 'zone_co2_1': 'empty', 'zone_co2_2': 'empty', 'load_type_1': 'empty',
            'load_type_2': 'empty', 'product_types_eex_1': 'empty', 'product_types_eex_2': 'week',
            'product_types_icis_1': 'week', 'product_types_icis_2': 'empty', 'product_types_tge_1': 'empty',
            'product_types_tge_2': 'empty', 'product_types_spot_1': 'empty', 'product_types_spot_2': 'empty',
            'product_types_co2_1': 'empty', 'product_types_co2_2': 'empty', 'period_week_1': 'week1',
            'period_week_2': 'week1', 'period_weekend_1': 'empty', 'period_weekend_2': 'empty',
            'period_month_1': 'empty', 'period_month_2': 'empty', 'period_quarter_1': 'empty',
            'period_quarter_2': 'empty', 'period_season_1': 'empty', 'period_season_2': 'empty',
            'period_year_1': 'empty', 'period_year_2': 'empty', 'period_gas_year_1': 'empty',
            'period_gas_year_2': 'empty', 'year_1': '2018', 'year_2': '2019', 'period_deliverystart_1': None,
            'period_deliverystart_2': None, 'period_deliveryend_1': None, 'period_deliveryend_2': None}

    a = Calculator(form)
