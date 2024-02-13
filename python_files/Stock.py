import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick  # optional may be helpful for plotting percentage
import numpy as np
import pandas as pd
import seaborn as sb  # optional to set plot theme

sb.set_theme()  # optional to set plot theme

DEFAULT_START = dt.date.isoformat(dt.date.today() - dt.timedelta(365))
DEFAULT_END = dt.date.isoformat(dt.date.today())


class Stock:
    def __init__(self, symbol, start=DEFAULT_START, end=DEFAULT_END):
        self.symbol = symbol
        self.start = start
        self.end = end
        self.data = self.get_data()

    def get_data(self):
        import yfinance as yf
        data = yf.download(self.symbol, start=self.start, end=self.end)
        data.index = pd.to_datetime(data.index)
        data.index.name = 'date'
        self.calc_returns(data)
        return data
        pass

    def calc_returns(self, df):
        df['Change'] = df['Close'].diff()
        df['Return'] = np.log(df['Close']).diff().round(4)
        pass

    def plot_return_dist(self):
        self.data['Return'].hist(bins=50, alpha=0.6)
        plt.show()
        pass

    def plot_performance(self):
        self.data['Cumulative Return'] = (1 + self.data['Return']).cumprod() - 1
        self.data['Cumulative Return'].plot()
        plt.show()
        pass


def main():
    symbol = "META"
    test = Stock(symbol=symbol)
    print(test.data)
    test.plot_performance()
    test.plot_return_dist()


if __name__ == '__main__':
    main()
