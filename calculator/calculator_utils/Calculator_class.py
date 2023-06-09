from calculator.dict_data.form_values import *
from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine
from decouple import config as envs
from pathlib import Path
import pandas as pd
import datetime
import time
import os


def get_dict_value(search_list, searched_value):
    for index, value in enumerate(search_list):
        if value[0] == searched_value:
            return value[1]


class Calculator:
    def __init__(self, form):
        self.form_1 = None
        self.form_2 = None
        self.clean_form(form)

        load_dotenv(find_dotenv())
        engine = create_engine(envs('ALCHEMY_CONNECTION', cast=str))
        self.conn = engine.raw_connection()

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
        q = "select trading_date, price_mid, delivery_year " \
            "from bi.icis_bi " \
            "left join bi.gas_icis_product gip on gip.prod_id = icis_bi.prod_id " \
            "left join bi.gas_icis_hub on gip.h_id = gas_icis_hub.h_id " \
            "left join bi.months m on delivery_month = month_num " \
            f"where h_name = '{hub}' and delivery_year >= 2018 " \
            f"and product_type = '{form_values['product_types_icis'].replace('_', ' ').title()}' "
        if form_values['product_types_icis'] == 'day':
            q += f"and delivery_start_date = '{form_values['period_deliverystart']}' order by trading_date;"

        elif form_values['product_types_icis'] == 'week':
            q += f"and extract('week' from delivery_start_date) = {form_values['period_week'].replace('week', '')} " \
                 f"and delivery_year <= {form_values['year']}"

        elif form_values['product_types_icis'] == 'weekend':
            q += f"and extract('week' from delivery_start_date) = {form_values['period_weekend'].replace('weekend', '')} " \
                 f"and delivery_year <= {form_values['year']}"

        elif form_values['product_types_icis'] == 'month':
            q += f"and month_name_eng = '{form_values['period_month'].capitalize()}' " \
                 f"and delivery_year <= {form_values['year']} order by trading_date"

        elif form_values['product_types_icis'] == 'quarter':
            q += f"and extract('quarter' from delivery_start_date) = {form_values['period_quarter'].replace('q', '')} " \
                 f"and delivery_year <= {form_values['year']} order by trading_date"

        elif form_values['product_types_icis'] == 'season':
            if form_values['period_season'] == 'gas_winter':
                q += f"and delivery_month = 10 " \
                     f"and delivery_year <= {form_values['year']} order by trading_date"
            elif form_values['period_season'] == 'gas_summer':
                q += f"and delivery_month = 4 " \
                     f"and delivery_year <= {form_values['year']} order by trading_date"

        elif form_values['product_types_icis'] == 'year':
            q += f"and delivery_year <= {form_values['period_year']} order by trading_date"

        elif form_values['product_types_icis'] == 'gas_year':
            q += f"and delivery_year <= {form_values['period_gas_year'].replace('gas_year_', '')} order by trading_date"

        df = self.get_table_from_query(q)
        if form_values == self.form_1:
            df.rename(columns={'price_mid': 'price_1'}, inplace=True)
        elif form_values == self.form_2:
            df.rename(columns={'price_mid': 'price_2'}, inplace=True)
        return df

    def get_eex_gas(self, form_values):
        hub = get_dict_value(HUBS['eex'], form_values['zone_eex_gas'])
        q = "select trading_date, settlement_price, delivery_year from bi.gas_futures_sftp_bi gfsb " \
            "left join bi.sftp_futures_type_ref sftr on sftr.id = gfsb.futures_type " \
            "left join bi.months m on m.month_num = gfsb.delivery_month " \
            "left join bi.sftp_hub_ref shr on gfsb.hub = shr.id " \
            "left join bi.sftp_product_type_ref sptr on gfsb.product_type = sptr.id " \
            f"where shr.hub = '{hub}' " \
            f"and sptr.product_type = '{form_values['product_types_eex'].replace('_', ' ').title()}' "
        if form_values['product_types_eex'] == 'day':
            q += f"and delivery_start_date = '{form_values['period_deliverystart']}' order by trading_date;"

        elif form_values['product_types_eex'] == 'week':
            q += f"and extract('week' from delivery_start_date) = {form_values['period_week'].replace('week', '')} " \
                 f"and delivery_year = {form_values['year']} order by trading_date;"

        elif form_values['product_types_eex'] == 'weekend':
            q += f"and extract('week' from delivery_start_date) = {form_values['period_weekend'].replace('weekend', '')} " \
                 f"and delivery_year = {form_values['year']} order by trading_date;"

        elif form_values['product_types_eex'] == 'month':
            q += f"and month_name_eng = '{form_values['period_month'].capitalize()}' " \
                 f"and delivery_year = {form_values['year']} order by trading_date"

        elif form_values['product_types_eex'] == 'quarter':
            q += f"and extract('quarter' from delivery_start_date) = {form_values['period_quarter'].replace('q', '')} " \
                 f"and delivery_year = {form_values['year']} order by trading_date"

        elif form_values['product_types_eex'] == 'season':
            if form_values['period_season'] == 'gas_winter':
                q += f"and delivery_month = 10 " \
                     f"and delivery_year = {form_values['year']} order by trading_date"
            elif form_values['period_season'] == 'gas_summer':
                q += f"and delivery_month = 4 " \
                     f"and delivery_year = {form_values['year']} order by trading_date"

        elif form_values['product_types_eex'] == 'year':
            q += f"and delivery_year = {form_values['period_year']} order by trading_date"

        df = self.get_table_from_query(q)
        if form_values == self.form_1:
            df.rename(columns={'settlement_price': 'price_1'}, inplace=True)
        elif form_values == self.form_2:
            df.rename(columns={'settlement_price': 'price_2'}, inplace=True)
        df = df.drop_duplicates()
        return df

    def get_ee_spot(self, form_values):
        zone = get_dict_value(DAM_ZONES['electricity_spot'], form_values['zone_ee_spot'])
        q = "select date_time, price, year as delivery_year from bi.power_da_prices_hourly_bi " \
            f"where bidding_zone = '{zone}' " \
            f"and date_time >= '{form_values['period_deliverystart']}' " \
            f"and date_time <= '{form_values['period_deliveryend']}'"

        df = self.get_table_from_query(q)
        if form_values == self.form_1:
            df.rename(columns={'date_time': 'trading_date', 'price': 'price_1'}, inplace=True)
        elif form_values == self.form_2:
            df.rename(columns={'date_time': 'trading_date', 'price': 'price_2'}, inplace=True)
        df = df.drop_duplicates()
        return df

    def get_ee_futures(self, form_values):
        if form_values['exchange_ee_futures'] == 'tge':
            q = f"select vtd.trading_date as trading_date, settlement_price * cur.ex_rate as settlement_price, " \
                f"delivery_year from bi.v_tge_data vtd left join " \
                f"(select date_stamp as trading_date, ex_rate " \
                f"from bi.currency_exchange_rates_bi where c_currency = 'EUR' and b_currency = 'PLN') " \
                f"cur on vtd.trading_date = cur.trading_date " \
                f"where load_type = '{form_values['load_type'].upper()}' "
            if form_values['product_types_tge'] == 'week':
                q += f"and product_type = 'Week' " \
                     f"and delivery_period = '{int(form_values['period_week'].replace('week', '')):02d}' " \
                     f"and delivery_year <= '{form_values['year']}' order by trading_date "
            elif form_values['product_types_tge'] == 'month':
                q += f"and product_type = 'Month' " \
                     f"and delivery_period = '{form_values['period_month'].capitalize()}' " \
                     f"and delivery_year <= '{form_values['year']}' order by trading_date "
            elif form_values['product_types_tge'] == 'quarter':
                q += f"and product_type = 'Quarter' " \
                     f"and delivery_period = '{form_values['period_quarter'].replace('q', '')}' " \
                     f"and delivery_year <= '{form_values['year']}' order by trading_date "
            elif form_values['product_types_tge'] == 'year':
                q += f"and product_type = 'Year' " \
                     f"and delivery_year <= '{form_values['period_year']}' order by trading_date "

        if form_values['exchange_ee_futures'] == 'eex':
            zone = get_dict_value(FUTURES['eex'], form_values['zone_ee_futures_eex'])
            q = f"select trading_date, settlement_price, delivery_year from bi.power_futures_sftp_bi pfsb " \
                f"left join bi.sftp_product_type_ref sptr on pfsb.product_type = sptr.id " \
                f"left join bi.sftp_zone_ref szr on pfsb.zone = szr.id " \
                f"left join bi.sftp_load_type_ref sltr on pfsb.load_type = sltr.id " \
                f"left join bi.months on pfsb.delivery_month = months.month_num " \
                f"where sptr.product_type = '{form_values['product_types_eex'].capitalize()}' " \
                f"and szr.zone = '{zone}' and sltr.load_type = '{form_values['load_type'].capitalize()}' "

            if form_values['product_types_eex'] == 'day':
                q += f"and delivery_start_date = '{form_values['period_deliverystart']}' order by trading_date"

            elif form_values['product_types_eex'] in 'week':
                q += f" and extract('week' from delivery_start_date) = {form_values['period_week'].replace('week', '')}"
                q += f" and delivery_year <= {form_values['year']} order by trading_date"

            elif form_values['product_types_eex'] == 'weekend':
                q += f" and extract('week' from delivery_start_date) = {form_values['period_weekend'].replace('weekend', '')}"
                q += f" and delivery_year <= {form_values['year']} order by trading_date"

            elif form_values['product_types_eex'] == 'month':
                q += f" and month_name_eng  = '{form_values['period_month'].capitalize()}'"
                q += f" and delivery_year <= {form_values['year']} order by trading_date"

            elif form_values['product_types_eex'] == 'quarter':
                q += f" and extract('quarter' from delivery_start_date) = {form_values['period_quarter'].replace('q', '')}"
                q += f" and delivery_year <= {form_values['year']} order by trading_date"

            elif form_values['product_types_eex'] == 'season':
                if form_values['period_season'] == 'gas_winter':
                    q += '  and delivery_month = 10'
                elif form_values['period_season'] == 'gas_summer':
                    q += '  and delivery_month = 4'
                q += f" and delivery_year <= {form_values['year']} order by trading_date"

            elif form_values['product_types_eex'] == 'year':
                q += f" and delivery_year <= {form_values['period_year']} order by trading_date"

        df = self.get_table_from_query(q)
        if form_values == self.form_1:
            df.rename(columns={'settlement_price': 'price_1'}, inplace=True)
        elif form_values == self.form_2:
            df.rename(columns={'settlement_price': 'price_2'}, inplace=True)

        return df

    def get_co2(self, form_values):
        q = f"select trading_date, settlement_price, extract('year' from delivery_period) as delivery_year " \
            f"from bi.eua_futures_sftp_bi efsb " \
            f"left join bi.sftp_emission_contract_ref secr on efsb.emission_contract = secr.id " \
            f"where secr.emission_contract = 'EUA' " \
            f"and replace(to_char(delivery_period, 'Month'), ' ', '') = '{form_values['period_month'].capitalize()}' " \
            f"and extract('year' from delivery_period) <= {form_values['year']} " \
            f"order by trading_date"

        df = self.get_table_from_query(q)
        if form_values == self.form_1:
            df.rename(columns={'settlement_price': 'price_1'}, inplace=True)
        elif form_values == self.form_2:
            df.rename(columns={'settlement_price': 'price_2'}, inplace=True)
        df['delivery_year'] = df['delivery_year'].astype(int)
        return df

    def get_data_for_form(self, form_data):
        if form_data['commodity'] == 'gas':
            if form_data['exchange_gas'] == 'icis':
                return self.get_icis(form_data)
            elif form_data['exchange_gas'] == 'eex':
                return self.get_eex_gas(form_data)
        elif form_data['commodity'] == 'electricity_spot':
            return self.get_ee_spot(form_data)
        elif form_data['commodity'] == 'electricity_futures':
            return self.get_ee_futures(form_data)
        elif form_data['commodity'] == 'co2':
            return self.get_co2(form_data)

    def merge_dfs(self, df1, df2):
        # NOTE pd.merge(df1, df2, how='inner', on=['trading_date', 'delivery_year']).drop_duplicates()
        df = pd.merge(df1, df2, how='inner', on=['trading_date', 'delivery_year']).drop_duplicates()
        df['delta'] = df['price_1'] - df['price_2']
        return df

    def rename_columns(self, df):
        form1 = {}
        form2 = {}
        for key, value in self.form_1.items():
            form1[key.split('_')[0]] = value

        for key, value in self.form_2.items():
            form2[key.split('_')[0]] = value

        df.rename(columns={
            'price_1': f"{form1['zone'].upper()} {form1['period'].title()} {form1['year']} ({form1['commodity'].upper()} {form1['exchange'].upper()})",
            'price_2': f"{form2['zone'].upper()} {form2['period'].title()} {form2['year']} ({form2['commodity'].upper()} {form2['exchange'].upper()})"}
            , inplace=True)

# TODO unify for all variants

        return df

    def run(self):
        df_1 = self.get_data_for_form(self.form_1)
        df_2 = self.get_data_for_form(self.form_2)
        df_1 = df_1.dropna()
        df_2 = df_2.dropna()
        df_1['delivery_year'] = df_1['delivery_year'].astype(int)
        df_2['delivery_year'] = df_2['delivery_year'].astype(int)
        df_1['trading_date'] = pd.to_datetime(df_1['trading_date'])
        df_2['trading_date'] = pd.to_datetime(df_2['trading_date'])
        df = self.merge_dfs(df_1, df_2)
        df = df[['trading_date', 'price_1', 'price_2', 'delta', 'delivery_year']]
        df = self.rename_columns(df)
        df['trading_date'] = df['trading_date'].astype('str')
        df = df.round(decimals=3)
        df.rename(columns={'trading_date': 'Trading Date', 'delta': 'Delta', 'delivery_year': 'Delivery Year'},
                  inplace=True)
        return df

    def rename_df(self, df):

        return df

    def get_table_from_query(self, query):
        with self.conn.cursor() as cur:
            cur.execute(query)
            df = pd.DataFrame(cur.fetchall(), columns=[d[0] for d in cur.description])
        return df


if __name__ == '__main__':
    form = {'commodity': 'co2', 'exchange_gas_1': 'empty', 'exchange_gas_2': 'empty', 'exchange_ee_spot_1': 'empty',
            'exchange_ee_spot_2': 'empty', 'exchange_ee_futures_1': 'empty', 'exchange_ee_futures_2': 'empty',
            'exchange_co2_1': 'eex', 'exchange_co2_2': 'eex', 'zone_icis_gas_1': 'empty', 'zone_icis_gas_2': 'empty',
            'zone_eex_gas_1': 'empty', 'zone_eex_gas_2': 'empty', 'zone_ee_spot_1': 'empty', 'zone_ee_spot_2': 'empty',
            'zone_ee_futures_tge_1': 'empty', 'zone_ee_futures_tge_2': 'empty', 'zone_ee_futures_eex_1': 'empty',
            'zone_ee_futures_eex_2': 'empty', 'zone_co2_1': 'eua', 'zone_co2_2': 'eua', 'load_type_1': 'empty',
            'load_type_2': 'empty', 'product_types_eex_1': 'empty', 'product_types_eex_2': 'empty',
            'product_types_icis_1': 'empty', 'product_types_icis_2': 'empty', 'product_types_tge_1': 'empty',
            'product_types_tge_2': 'empty', 'product_types_spot_1': 'empty', 'product_types_spot_2': 'empty',
            'product_types_co2_1': 'month', 'product_types_co2_2': 'month', 'period_week_1': 'empty',
            'period_week_2': 'empty', 'period_weekend_1': 'empty', 'period_weekend_2': 'empty',
            'period_month_1': 'january', 'period_month_2': 'january', 'period_quarter_1': 'empty',
            'period_quarter_2': 'empty', 'period_season_1': 'empty', 'period_season_2': 'empty',
            'period_year_1': 'empty', 'period_year_2': 'empty', 'period_gas_year_1': 'empty',
            'period_gas_year_2': 'empty', 'year_1': '2023', 'year_2': '2022', 'period_deliverystart_1': None,
            'period_deliverystart_2': None, 'period_deliveryend_1': None, 'period_deliveryend_2': None}

    a = Calculator(form).run()
