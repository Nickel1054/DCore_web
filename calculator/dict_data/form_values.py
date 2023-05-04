from sqlalchemy import create_engine
# from decouple import config as envs
from dotenv import load_dotenv, find_dotenv
import psycopg2
import ast
import os

EXCHANGE = {
    "gas":
        [
            ('empty', '--'),
            ("icis", "ICIS"),
            ("eex", "EEX"),
        ],
    "clean_spark":
        [
            ("gas", "Gas"),
            ("icis", "ICIS"),
            ("eex_co2", "EEX + CO2")
        ],
    "spark":
        [
            ("icis", "ICIS"),
            ("eex", "EEX"),
        ],
    "electricity_spot":
        [
            ("spot", "Spot prices"),
        ],
    "electricity_futures":
        [
            ("tge", "TGE"),
            ("eex", "EEX"),
        ],
    "co2":
        [
            ("eex", "EEX"),
        ],
}

HUBS = {
    'eex': ['CEGH', 'CZECH', 'GPL', 'LTC', 'LTC', 'LTC', 'LTC', 'NBP', 'NCG', 'PEG', 'PSV', 'PVB', 'THE', 'TTF',
            'TURKISHGAS', 'UAVTP', 'VOB', 'ZEE', 'ZTP'],
    'icis': ['AT', 'CEGH', 'CZ VTP', 'ETF', 'Gaspool', 'LNG', 'NBP', 'NCG', 'PEG', 'PSV', 'PVB', 'THE', 'TTF',
             'ZEE', 'ZTP']
}


def get_hubs(source):
    load_dotenv(find_dotenv())
    engine = create_engine(os.getenv('ALCHEMY_CONNECTION'))
    conn = engine.raw_connection()
    cur = conn.cursor()

    if source == 'icis':
        cur.execute('select hub as hub from bi.sftp_hub_ref;')
    elif source == 'eex':
        cur.execute('select h_name as hub from bi.gas_icis_hub;')
    hubs = [item for sublist in cur.fetchall() for item in sublist]
    hubs.sort()
    return hubs


def get_zones_ee_spot():
    load_dotenv(find_dotenv())
    engine = create_engine(os.getenv('ALCHEMY_CONNECTION'))
    conn = engine.raw_connection()
    cur = conn.cursor()

    cur.execute('select distinct bidding_zone from bi.power_da_prices_hourly_bi order by bidding_zone;')
    zones = [item for sublist in cur.fetchall() for item in sublist]
    zones.sort()
    return zones


def get_zones_futures_eex():
    load_dotenv(find_dotenv())
    engine = create_engine(os.getenv('ALCHEMY_CONNECTION'))
    conn = engine.raw_connection()
    cur = conn.cursor()

    cur.execute('select distinct zone from bi.sftp_zone_ref order by zone;')
    zones = [item for sublist in cur.fetchall() for item in sublist]
    zones.sort()
    return zones


if __name__ == '__main__':
    # get_zones_futures_eex()
    pass
