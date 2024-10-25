import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def Quantity(df):
    quantity_by_country = df.groupby('Country')['UnitsInStock'].sum().sort_values(ascending=False).head(10)

    plt.figure(figsize=(10,6))
    sns.barplot(x=quantity_by_country.index, y=quantity_by_country.values)
    plt.title('Quantity by Country')
    plt.xlabel('Country')
    plt.ylabel('Quantity')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()