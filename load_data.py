import matplotlib.pyplot as plt
import pandas as pd

def analyze_pandas_csv(data):
    print('Header row')
    print (data.head())
    print('Shape')
    print(data.shape)
    print('10th row')
    print(data.iloc[10:11,:])
    print ('Index')
    print (data.index)
    print ('Describe:')
    print (data.describe())
    print ('Transposed:')
    print (data.T)
    print ('Pivot table')

    # pivot = data.pivot_table(values=['home_score','away_score'], index=['date'], columns=['country'])
    #print(pivot)



def create_series(data):
    #filter by date example: 
    #lines = data.loc['2015-01-01':'2020-01-01'].plot.line() 
    lines = data.plot.line()  
    plt.show()

print('Analyzing soccer scores csv')
d = pd.read_csv('./data_files/results.csv', parse_dates=True)
analyze_pandas_csv(d)
create_series(d)

print('Analyzing S&p 500 prices')
d2 = data = pd.read_csv('./data_files/spx.csv',parse_dates=True)
analyze_pandas_csv(d2)
create_series(d2)
