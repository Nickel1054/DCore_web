from sqlalchemy import create_engine
from dotenv import load_dotenv, find_dotenv
import psycopg2
import ast
import os

COMMODITIES = [
    ('empty', '--'),
    ('gas', 'Gas'),
    # ('clean_spark', 'Clean spark spread'),
    # ('spark', 'Spark spread'),
    ('electricity_spot', 'Electricity spot'),
    ('electricity_futures', 'Electricity futures'),
    ('co2', 'CO2'),
]

EXCHANGE = {
    "gas":
        [
            ('empty', '--'),
            ("icis", "ICIS"),
            ("eex", "EEX"),
        ],
    # "clean_spark":
    #     [
    #         ("gas", "Gas"),
    #         ("icis", "ICIS"),
    #         ("eex_co2", "EEX + CO2")
    #     ],
    # "spark":
    #     [
    #         ("icis", "ICIS"),
    #         ("eex", "EEX"),
    #     ],
    "electricity_spot":
        [
            ('empty', '--'),
            ("spot", "Spot prices"),
        ],
    "electricity_futures":
        [
            ('empty', '--'),
            ("tge", "TGE"),
            ("eex", "EEX"),
        ],
    "co2":
        [
            ('empty', '--'),
            ("eex", "EEX"),
        ],
}

HUBS = {
    'eex': [('empty', '--'), ('cegh', 'CEGH'), ('czech', 'CZECH'), ('gpl', 'GPL'), ('ltc', 'LTC'), ('nbp', 'NBP'),
            ('ncg', 'NCG'), ('peg', 'PEG'), ('psv', 'PSV'), ('pvb', 'PVB'), ('the', 'THE'), ('ttf', 'TTF'),
            ('turkishgas', 'TURKISHGAS'), ('uavtp', 'UAVTP'), ('vob', 'VOB'), ('zee', 'ZEE'), ('ztp', 'ZTP')],
    'icis': [('empty', '--'), ('at', 'AT'), ('cegh', 'CEGH'), ('cz_vtp', 'CZ VTP'), ('etf', 'ETF'),
             ('gaspool', 'Gaspool'), ('lng', 'LNG'), ('nbp', 'NBP'), ('ncg', 'NCG'), ('peg', 'PEG'), ('psv', 'PSV'),
             ('pvb', 'PVB'), ('the', 'THE'), ('ttf', 'TTF'), ('zee', 'ZEE'), ('ztp', 'ZTP')]
}

DAM_ZONES = {
    'electricity_spot': [
        ('empty', '--'), ('at', 'AT'), ('be', 'BE'), ('bg', 'BG'), ('ch', 'CH'), ('cz', 'CZ'), ('de_lu', 'DE_LU'),
        ('dk_1', 'DK_1'), ('dk_2', 'DK_2'), ('ee', 'EE'), ('es', 'ES'), ('fi', 'FI'), ('fr', 'FR'), ('gb', 'GB'),
        ('gr', 'GR'), ('hr', 'HR'), ('hu', 'HU'), ('it_cnor', 'IT_CNOR'), ('it_csud', 'IT_CSUD'),
        ('it_nord', 'IT_NORD'), ('it_pun', 'IT_PUN'), ('it_rosn', 'IT_ROSN'), ('it_sard', 'IT_SARD'),
        ('it_sici', 'IT_SICI'), ('it_sud', 'IT_SUD'), ('lt', 'LT'), ('lv', 'LV'), ('me', 'ME'), ('nl', 'NL'),
        ('no_1', 'NO_1'), ('no_2', 'NO_2'), ('no_3', 'NO_3'), ('no_4', 'NO_4'), ('no_5', 'NO_5'), ('pl', 'PL'),
        ('pt', 'PT'), ('ro', 'RO'), ('rs', 'RS'), ('se_1', 'SE_1'), ('se_2', 'SE_2'), ('se_3', 'SE_3'),
        ('se_4', 'SE_4'), ('si', 'SI'), ('sk', 'SK'), ('tr', 'TR'), ('ua_ips', 'UA_IPS')
    ]
}

FUTURES = {
    'tge': [
        ('empty', '--'), ('tge', 'TGE')
    ],
    'eex': [
        ('empty', '--'), ('at', 'AT'), ('be', 'BE'), ('bg', 'BG'), ('ch', 'CH'), ('cz', 'CZ'), ('de', 'DE'),
        ('de_at', 'DE_AT'), ('es', 'ES'), ('fr', 'FR'), ('gb', 'GB'), ('gr', 'GR'), ('hu', 'HU'), ('it', 'IT'),
        ('jpk', 'JPK'), ('jpt', 'JPT'), ('nl', 'NL'), ('nord', 'NORD'), ('pl', 'PL'), ('ro', 'RO'), ('rs', 'RS'),
        ('si', 'SI'), ('sk', 'SK')
    ]
}

CO2 = {
    'eex': [
        ('empty', '--'), ('eua', 'EUA')
    ]
}

LOAD_TYPES = [
    ('empty', '--'), ('base', 'BASE'), ('peak', 'PEAK'),
]

PRODUCT_TYPES = {
    'eex': [
        [('day', 'Day'), ('week', 'Week'), ('weekend', 'Weekend'), ('month', 'Month'), ('quarter', 'Quarter'),
         ('season', 'Season'), ('year', 'Year'), ('season', 'Season')]
    ],
    'icis': [
        ('day', 'Day'), ('week', 'Week'), ('weekend', 'Weekend'), ('month', 'Month'), ('quarter', 'Quarter'),
        ('season', 'Season'), ('year', 'Year'), ('gas_year', 'Gas Year')

    ]
}


def get_hubs(source):
    load_dotenv(find_dotenv())
    engine = create_engine(os.getenv('ALCHEMY_CONNECTION'))
    conn = engine.raw_connection()
    cur = conn.cursor()

    if source == 'icis':
        cur.execute('select distinct hub as hub from bi.sftp_hub_ref;')
    elif source == 'eex':
        cur.execute('select distinct h_name as hub from bi.gas_icis_hub;')
    hubs = [item for sublist in cur.fetchall() for item in sublist]
    hubs.sort()
    ls = []
    for el in hubs:
        ls.append((el.lower(), el))
    return hubs


def get_zones_ee_spot():
    load_dotenv(find_dotenv())
    engine = create_engine(os.getenv('ALCHEMY_CONNECTION'))
    conn = engine.raw_connection()
    cur = conn.cursor()

    cur.execute('select distinct bidding_zone from bi.power_da_prices_hourly_bi order by bidding_zone;')
    zones = [item for sublist in cur.fetchall() for item in sublist]
    # zones.sort()
    ls = []
    for el in zones:
        ls.append((el.lower(), el))
    return zones


def get_zones_futures_eex():
    load_dotenv(find_dotenv())
    engine = create_engine(os.getenv('ALCHEMY_CONNECTION'))
    conn = engine.raw_connection()
    cur = conn.cursor()

    cur.execute('select distinct zone from bi.sftp_zone_ref order by zone;')
    zones = [item for sublist in cur.fetchall() for item in sublist]
    zones.sort()
    ls = []
    for el in zones:
        ls.append((el.lower(), el))
    return ls


def get_product_types(source):
    load_dotenv(find_dotenv())
    engine = create_engine(os.getenv('ALCHEMY_CONNECTION'))
    conn = engine.raw_connection()
    cur = conn.cursor()

    if source == 'eex':
        cur.execute(
            "select distinct product_type from bi.sftp_product_type_ref where length(product_type) >= 3 and product_type != 'N/A' order by product_type;")
    elif source == 'icis':
        cur.execute("select distinct product_type from bi.gas_icis_product;")
    product_types = [item for sublist in cur.fetchall() for item in sublist]
    product_types.sort()
    ls = []
    for el in product_types:
        ls.append((el.lower().replace(' ', '_'), el))
    return 0


if __name__ == '__main__':
    ls = get_product_types('icis')
    pass
