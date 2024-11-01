import pandas as pd
import altair as alt

alt.renderers.enable('html')
alt.renderers.set_embed_options(actions=True)

def Sales(df):
    sales_by_category = df.groupby(['Category','Discount'])['Sales'].sum().reset_index()

    sales_by_category['SalesWithoutDiscount'] = sales_by_category.apply(lambda r: (r['Sales'] if r['Discount'] == 0 else None), axis=1)

    sales_by_category['SalesWithDiscount'] = sales_by_category.apply(lambda r: (r['Sales'] if r['Discount'] > 0 else None), axis=1)

    sales = sales_by_category.groupby('Category')[['SalesWithDiscount', 'SalesWithoutDiscount']].sum()

    #sales_by_category['DiscountSales'] = sales_by_category.apply(lambda r: (r['Sales'] * (1 - r['Discount']) if 0 <= r['Discount'] < 1 else r['Sales']), axis=1)

    sales_melted = pd.melt(sales, value_vars=['SalesWithDiscount', 'SalesWithoutDiscount'])
    
    chart = alt.Chart(sales).mark_bar().encode(x='Category:N', y='Sales:Q', color='type:N').properties(width=600, height=400, title='Sales by category').interactive()

    chart.show()