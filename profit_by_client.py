import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import hvplot.pandas
import warnings

warnings.filterwarnings('ignore')

def profit_by_client(df):
    profit_by_customer = df.groupby(['Customer'])['Profit'].sum().sort_values(ascending=False).head(10)
    plt.figure(figsize=(10,6))
    sns.barplot(x=profit_by_customer.index, y=profit_by_customer.values)
    plt.title('Profit by client')
    plt.xlabel('Client')
    plt.ylabel('Profit')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    customer_category = df.groupby(['Customer', 'Category'])[['Profit', 'Sales']].sum().reset_index()

    top_customers = customer_category[customer_category['Customer'].isin(profit_by_customer.index)]

    plot = top_customers.hvplot.bar(x='Customer', y='Profit', by='Category', title='Profit by category', xlabel='Customer', ylabel='Profit', stacked=True)
    hvplot.show(plot)