import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#=================================
#    DATA CREATION
#=================================
np.random.seed(33)
rows_number=1000
def create_data():
    categories = ['Electronics', 'Apparel', 'Home & Kitchen', 'Books', 'Beauty']
    payments = ['Credit Card', 'PayPal', 'Debit Card', 'Cash']

    data={
        "Transaction_id":[f"TN-{1000+i}" for i in range(rows_number)],
        "Date":pd.date_range(start='2026-01-01',end='2026-12-31',periods=rows_number),
        "Category":np.random.choice(categories,rows_number,p=[0.3,0.2,0.1,0.3,0.1]),
        "Quantity":np.random.randint(1,6,rows_number),
        "UnitPrice":np.random.uniform(12.0,300.0,rows_number),
        "Discount":np.where(np.random.rand(rows_number)>0.75,0.15,0.0),
        "PaymentMethod":np.random.choice(payments,rows_number,p=[0.3,0.2,0.2,0.3])}

    return pd.DataFrame(data)


#DATA CLEANING 
def clean_data(df):
    df["GrossSales"]=df["Quantity"]*df["UnitPrice"]
    df["NetSales"]=df["GrossSales"]*(1-df["Discount"])
    df["Month"]=df["Date"].dt.to_period('M')
    return df







#EXCUTION 
df=create_data()
df=clean_data(df)
print(df)