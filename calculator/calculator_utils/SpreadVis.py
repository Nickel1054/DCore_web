import urllib.parse

import base64

from dateutil.relativedelta import relativedelta
import matplotlib.transforms as mtransforms
import matplotlib.ticker as ticker
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime
import pickle
import io


class SpreadVis:
    def __init__(self, df):
        self.__df = df
        self.__sell_name = None
        self.__buy_name = None
        self.__modify_df()
        self.__number_of_years = 4

    def __modify_df(self):
        cols = self.__df.columns.tolist()
        self.__buy_name = [s for s in cols if ' BUY' in s][0].replace(' BUY', '')
        self.__sell_name = [s for s in cols if ' SELL' in s][0].replace(' SELL', '')
        cols = ['BUY' if ' BUY' in item else item for item in cols]
        cols = ['SELL' if ' SELL' in item else item for item in cols]
        self.__df.columns = cols
        self.__df['Trading Date'] = pd.to_datetime(self.__df['Trading Date'])

    def get_df(self):
        return self.__df

    def create_spread_plot(self, df, ax):
        ax.plot(df['Trading Date'], df['Spread'], '-g.', c='grey', markevery=None, label='Spread')
        ax.set_ylabel('Spread')
        ax.axhline(y=0, linestyle='-', linewidth=2, color='black')
        # self.annot_max(df['Trading Date'], df['Spread'], ax)

    def create_curve_plot(self, df, ax):
        ax.plot(df['Trading Date'], df['BUY'], '-r.', markevery=None, label='Buy')
        ax.plot(df['Trading Date'], df['SELL'], '-b.', markevery=None, label='Sell')
        ax.set_ylabel('Price')
        # self.annot_max(df['Trading Date'], df['BUY'], ax)
        # self.annot_max(df['Trading Date'], df['SELL'], ax)

    def create_plot(self, ax, year, column):
        df = self.__df.loc[self.__df['Delivery Year'] == year]
        if column == 0:
            self.create_curve_plot(df, ax)
        elif column == 1:
            self.create_spread_plot(df, ax)

        if df['Trading Date'].max() - df['Trading Date'].min() > datetime.timedelta(days=6 * 30):
            ax.xaxis.set_major_locator(mdates.MonthLocator())  # bymonth=months))  # bymonth=(1, 3, 5, 7, 9, 11)))
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%b'))
        else:
            ax.xaxis.set_major_locator(ticker.MaxNLocator(12))
        ax.yaxis.set_major_locator(ticker.MaxNLocator(5))
        ax.yaxis.set_minor_locator(ticker.AutoMinorLocator(2))
        ax.grid(True)
        ax.grid(True, which='minor', linestyle='--')

        ax.title.set_text(f'Delivery Year {year}')


        for label in ax.get_xticklabels(which='major'):
            label.set(rotation=30, horizontalalignment='right')

        ax.legend(fontsize='large')

    def run(self):
        # df = self.__df.loc[self.__df['Trading Date'] > max(self.__df['Trading Date']) - relativedelta(months=6)]
        df = self.get_df()
        years = df['Delivery Year'].unique().tolist()
        years.sort(reverse=False)
        num_of_rows = min(self.__number_of_years, len(years))
        if num_of_rows < 1:
            return None
        fig, axs = plt.subplots(num_of_rows, 2, figsize=(15, 4 * num_of_rows),
                                layout='constrained')

        if axs.ndim == 1:
            axs = [axs]

        for row in range(num_of_rows):
            for column in [0, 1]:
                self.create_plot(axs[row][column], years[row], column)

        # plt.legend(fontsize='large')
        fig.suptitle(f'BUY: {self.__buy_name}\nSELL: {self.__sell_name}')

        # fig.savefig('fig1.png', bbox_inches=mtransforms.Bbox([[0, 0], [0.5, 0.25]]).transformed(
        #     (fig.transFigure - fig.dpi_scale_trans)))

        # fig.savefig('fig.png')

        return self.convert_to_data(fig)

    @staticmethod
    def convert_to_data(fig):
        imgdata = io.BytesIO()
        fig.savefig(imgdata, format='png')
        imgdata.seek(0)
        # graph = imgdata.getvalue()
        string = base64.b64encode(imgdata.read())
        graph = urllib.parse.quote(string)
        return graph

    @ staticmethod
    def annot_max(x, y, ax):
        xmax = x.tolist()[np.argmax(y)]
        ymax = y.max()
        text = "x={:}, y={:.3f}".format(xmax, ymax)
        if not ax:
            ax = plt.gca()
        bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
        arrowprops = dict(arrowstyle="->", connectionstyle="angle,angleA=0,angleB=60")
        kw = dict(xycoords='data', textcoords="axes fraction",
                  arrowprops=arrowprops, bbox=bbox_props, ha="right", va="top")
        ax.annotate(text, xy=(xmax, ymax), xytext=(0.94, 0.96), **kw)


if __name__ == '__main__':
    data = pd.read_csv('df.csv', index_col=0)
    # data = data.rename(columns={data.columns[1]: 'BUY'})
    SpreadVis(data).run()
    print(111)
