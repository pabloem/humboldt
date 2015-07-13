import pandas as pd
import pandas.io.data
from dateutil.parser import parse

class DataManager(object):
    def __init__(self,options):
        if type(options) != dict:
            options = {}
        self._tickers = options['tickers']
        self._startDate = parse(options['start_date'])
        self._endDate = parse(options['end_date'])
    def getData(self):
        self._df = pd.io.data.get_data_yahoo(self._tickers,
                                             self._startDate,
                                             self._endDate)
    def massageData(self):
        if not hasattr(self, '_df'):
            self.getData()
        self._df.pct_change()
