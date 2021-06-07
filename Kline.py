import tushare as ts
import mplfinance as mpf
import matplotlib as mpl  # 用于设置曲线参数
from cycler import cycler  # 用于定制线条颜色
import pandas as pd  # 导入DataFrame数据
import matplotlib.pyplot as plt

df = ts.get_k_data('000012',start = "2019-05-27",end = '2021-05-27')
print(df) #打印检查导入数据
df.rename(columns={'date': 'Date', 'open': 'Open','high': 'High', 'low': 'Low','close': 'Close', 'volume': 'Volume'},inplace=True)
df['Date'] = pd.to_datetime(df['Date'])# 转换为日期格式
df.set_index(['Date'], inplace=True)# 将日期列作为行索引
number = '000012' #命名
#绘制动态图
for i in range(1,len(df),1):
    #重复绘图
    plt.ion()
    plt.grid()
    kwargs = dict(
        type='candle',
        mav=(5, 10, 30),
        volume=False,
        title='\n%skline' % (number),
        ylabel='OHLC Candles',
        ylabel_lower='Shares\nTraded Volume',
        figratio=(15, 10),
        figscale=5)
    mc = mpf.make_marketcolors(
        up='red',
        down='green',
        edge='i',
        wick='i',
        volume='in',
        inherit=True)
    s = mpf.make_mpf_style(
        gridaxis='both',
        gridstyle='-.',
        y_on_right=False,
        marketcolors=mc)
    mpl.rcParams['axes.prop_cycle'] = cycler(
        color=['dodgerblue', 'deeppink',
               'navy', 'teal', 'maroon', 'darkorange',
               'indigo'])
    mpl.rcParams['lines.linewidth'] = .5  # 线宽
    mpf.plot(df.iloc[0:i],
             **kwargs,
             style=s,
             show_nontrading=False)
    plt.pause(0.1)
    plt.ioff()