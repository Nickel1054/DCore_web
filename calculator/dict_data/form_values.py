from sqlalchemy import create_engine
from dotenv import load_dotenv, find_dotenv
import calendar
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
    'icis': [('empty', '--'), ('cegh', 'CEGH'), ('czech', 'CZECH'), ('gpl', 'GPL'), ('ltc', 'LTC'), ('nbp', 'NBP'),
            ('ncg', 'NCG'), ('peg', 'PEG'), ('psv', 'PSV'), ('pvb', 'PVB'), ('the', 'THE'), ('ttf', 'TTF'),
            ('turkishgas', 'TURKISHGAS'), ('uavtp', 'UAVTP'), ('zee', 'ZEE'), ('ztp', 'ZTP')],
    'eex': [('empty', '--'), ('at', 'AT'), ('cegh', 'CEGH'), ('cz_vtp', 'CZ VTP'), ('etf', 'ETF'),
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
        ('empty', '--'), ('tge', 'PL')
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
        ('empty', '--'), ('day', 'Day'), ('week', 'Week'), ('weekend', 'Weekend'), ('month', 'Month'),
        ('quarter', 'Quarter'), ('season', 'Season'), ('year', 'Year')
    ],
    'icis': [
        ('empty', '--'), ('day', 'Day'), ('week', 'Week'), ('weekend', 'Weekend'), ('month', 'Month'),
        ('quarter', 'Quarter'), ('season', 'Season'), ('year', 'Year'), ('gas_year', 'Gas Year')
    ],
    'tge': [
        ('empty', '--'), ('week', 'Week'), ('month', 'Month'), ('quarter', 'Quarter'), ('year', 'Year')
    ],
    'spot': [
        ('empty', '--'), ('da', 'DA'),
    ],
    'co2': [
        ('empty', '--'), ('month', 'Month'),
    ],
}

DELIVERY_PERIOD = {
    'week': [
        ('empty', '--'),
        ('week1', 'Week 1'), ('week2', 'Week 2'), ('week3', 'Week 3'), ('week4', 'Week 4'), ('week5', 'Week 5'),
        ('week6', 'Week 6'), ('week7', 'Week 7'), ('week8', 'Week 8'), ('week9', 'Week 9'), ('week10', 'Week 10'),
        ('week11', 'Week 11'), ('week12', 'Week 12'), ('week13', 'Week 13'), ('week14', 'Week 14'),
        ('week15', 'Week 15'), ('week16', 'Week 16'), ('week17', 'Week 17'), ('week18', 'Week 18'),
        ('week19', 'Week 19'), ('week20', 'Week 20'), ('week21', 'Week 21'), ('week22', 'Week 22'),
        ('week23', 'Week 23'), ('week24', 'Week 24'), ('week25', 'Week 25'), ('week26', 'Week 26'),
        ('week27', 'Week 27'), ('week28', 'Week 28'), ('week29', 'Week 29'), ('week30', 'Week 30'),
        ('week31', 'Week 31'), ('week32', 'Week 32'), ('week33', 'Week 33'), ('week34', 'Week 34'),
        ('week35', 'Week 35'), ('week36', 'Week 36'), ('week37', 'Week 37'), ('week38', 'Week 38'),
        ('week39', 'Week 39'), ('week40', 'Week 40'), ('week41', 'Week 41'), ('week42', 'Week 42'),
        ('week43', 'Week 43'), ('week44', 'Week 44'), ('week45', 'Week 45'), ('week46', 'Week 46'),
        ('week47', 'Week 47'), ('week48', 'Week 48'), ('week49', 'Week 49'), ('week50', 'Week 50'),
        ('week51', 'Week 51'), ('week52', 'Week 52')
    ],
    'weekend': [
        ('empty', '--'),
        ('weekend1', 'Weekend 1'), ('weekend2', 'Weekend 2'), ('weekend3', 'Weekend 3'), ('weekend4', 'Weekend 4'),
        ('weekend5', 'Weekend 5'), ('weekend6', 'Weekend 6'), ('weekend7', 'Weekend 7'), ('weekend8', 'Weekend 8'),
        ('weekend9', 'Weekend 9'), ('weekend10', 'Weekend 10'), ('weekend11', 'Weekend 11'),
        ('weekend12', 'Weekend 12'), ('weekend13', 'Weekend 13'), ('weekend14', 'Weekend 14'),
        ('weekend15', 'Weekend 15'), ('weekend16', 'Weekend 16'), ('weekend17', 'Weekend 17'),
        ('weekend18', 'Weekend 18'), ('weekend19', 'Weekend 19'), ('weekend20', 'Weekend 20'),
        ('weekend21', 'Weekend 21'), ('weekend22', 'Weekend 22'), ('weekend23', 'Weekend 23'),
        ('weekend24', 'Weekend 24'), ('weekend25', 'Weekend 25'), ('weekend26', 'Weekend 26'),
        ('weekend27', 'Weekend 27'), ('weekend28', 'Weekend 28'), ('weekend29', 'Weekend 29'),
        ('weekend30', 'Weekend 30'), ('weekend31', 'Weekend 31'), ('weekend32', 'Weekend 32'),
        ('weekend33', 'Weekend 33'), ('weekend34', 'Weekend 34'), ('weekend35', 'Weekend 35'),
        ('weekend36', 'Weekend 36'), ('weekend37', 'Weekend 37'), ('weekend38', 'Weekend 38'),
        ('weekend39', 'Weekend 39'), ('weekend40', 'Weekend 40'), ('weekend41', 'Weekend 41'),
        ('weekend42', 'Weekend 42'), ('weekend43', 'Weekend 43'), ('weekend44', 'Weekend 44'),
        ('weekend45', 'Weekend 45'), ('weekend46', 'Weekend 46'), ('weekend47', 'Weekend 47'),
        ('weekend48', 'Weekend 48'), ('weekend49', 'Weekend 49'), ('weekend50', 'Weekend 50'),
        ('weekend51', 'Weekend 51'), ('weekend52', 'Weekend 52')
    ],
    'month': [
        ('empty', '--'),
        ('january', 'January'), ('february', 'February'), ('march', 'March'), ('april', 'April'), ('may', 'May'),
        ('june', 'June'), ('july', 'July'), ('august', 'August'), ('september', 'September'), ('october', 'October'),
        ('november', 'November'), ('december', 'December')
    ],
    'quarter': [
        ('empty', '--'), ('q1', 'Q1'), ('q2', 'Q2'), ('q3', 'Q3'), ('q4', 'Q4')
    ],
    'season': [
        ('empty', '--'), ('gas_winter', 'Gas Winter'), ('gas_summer', 'Gas Summer')
    ],
    'year': [
        ('empty', '--'),
        ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023'),
        ('2024', '2024'), ('2025', '2025')
    ],
    'gas_year': [
        ('empty', '--'),
        ('gas_year_2018', 'Gas Year 2018'), ('gas_year_2019', 'Gas Year 2019'), ('gas_year_2020', 'Gas Year 2020'),
        ('gas_year_2021', 'Gas Year 2021'), ('gas_year_2022', 'Gas Year 2022'), ('gas_year_2023', 'Gas Year 2023'),
        ('gas_year_2024', 'Gas Year 2024'), ('gas_year_2025', 'Gas Year 2025')
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
    elif source == 'tge':
        cur.execute("select distinct product_type from bi.v_tge_data;")
    product_types = [item for sublist in cur.fetchall() for item in sublist]
    product_types.sort()
    ls = []
    for el in product_types:
        ls.append((el.lower().replace(' ', '_'), el))
    return 0


def get_delivery_period(period: str):
    delivery_periods = []
    if period in ('week', 'weekend'):
        for i in range(1, 53):
            delivery_periods.append((period + f'{i}', period.capitalize() + f' {i}'))
    elif period == 'month':
        for i in range(1, 13):
            delivery_periods.append((calendar.month_name[i].lower(), calendar.month_name[i]))
    elif period == 'quarter':
        for i in range(1, 5):
            delivery_periods.append((f'q{i}', f'Q{i}'))
    elif period == 'year':
        for i in range(2018, 2026):
            delivery_periods.append((f'{i}', f'{i}'))
    elif period == 'gas_year':
        for i in range(2018, 2026):
            delivery_periods.append((f'gas_year_{i}', f'Gas Year {i}'))
    return 0


if __name__ == '__main__':
    # ls = get_product_types('eex')
    get_delivery_period('gas_year')
    pass
