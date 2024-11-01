import warnings
from data import Open
from profit_by_client import profit_by_client
from quantity_by_country import Quantity
from sales_by_category import Sales
from creativity import Profit

warnings.filterwarnings('ignore')

def run():
    filepath = 'Product_Gallery.xlsx'
    df = Open(filepath)
    if df is None:
        print('Error: Failed to open dataset')
        return
    elif df.empty:
        print('Error: Dataset is empty')
        return
    
    profit_by_client(df)
    Quantity(df)
    Sales(df)
    Profit(df)

if __name__ == '__main__':
    run()