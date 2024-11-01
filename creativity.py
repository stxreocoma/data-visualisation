#АНАЛИЗ САМАЯ ПРИБЫЛЬНАЯ КАТЕГОРИЯ ТОВАРОВ ПО ГОРОДАМ
import pandas as pd
import numpy as np
import panel as pn
import hvplot.pandas

def Profit(df):
    df['ProfitPerUnit'] = df['Profit'] / np.where(df['Sales'] > 0, df['Sales'], 1)

    #df['MeanProfitPerUnitByCategory'] = df.groupby('Category')['ProfitPerUnit'].mean()

    profit_per_unit_by_category_and_city = df.groupby(['City and Counry', 'Category'])['ProfitPerUnit'].mean().reset_index()

    print(profit_per_unit_by_category_and_city)

    plot = profit_per_unit_by_category_and_city.hvplot.bar(x='City and Counry', y='ProfitPerUnit', by='Category', title='Profit per unit by city and category', xlabel='City and Country', ylabel='Profit', stacked=True)
    hvplot.show(plot)