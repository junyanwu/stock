import pandas as pd
import baostock as bs
import math
import time
from datetime import datetime


class Data():
    def __init__(self):
        pass

    def getStockDay(self):
        '''

        :return:`
        '''

def get_stock_basic(type, save=False):
    '''
    获取所有股票基本信息，并且返回type类型的数据
    :param type: 选择希望返回的数据
    :param save: 选择是否保存股票基本信息
    :return: 返回type类型的数据
    '''
    stock_basic = bs.query_stock_basic()
    res = pd.DataFrame(stock_basic.data, columns=stock_basic.fields)
    if save:
        res.to_csv("D:\quant\BaoStock\data\stock_basic.csv", index=False)
    if type=='code-ipoDate':
        return res['code'].values, res['ipoDate'].values
    else:
        return res


def get_stock_history_k_data(code, start_date,
                             end_date=time.strftime("%Y-%m-%d", time.localtime()),
                             save=False):
    '''

    :param code: 股票代码
    :param start_date:  format "2020-10-01"
    :param end_date: format "2020-10-01"
    :return:
    '''
    res = bs.query_history_k_data_plus(code=code,
                                       fields="date,code,open,high,low,close,preclose,volume,amount,adjustflag,turn,tradestatus,pctChg,isST",
                                       start_date=start_date, end_date=end_date)
    if save:
        history_k = pd.DataFrame(res.data, columns=res.fields)
        history_k.to_csv('D:\quant\BaoStock\data\%s' % code, index=False)
    print(res)


if __name__ == '__main__':
    lg = bs.login()
    # 获取目前上市的stock
    code, ipoDate = get_stock_basic(save=True, type='code-ipoDate')
    # 获取上市公司code的历史k线走势
    for _code, _date in zip(code, ipoDate):
        get_stock_history_k_data(_code, _date, save=True)