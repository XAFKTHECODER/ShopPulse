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

#==============================
#DATA CLEANING & FEAUTURE ENGINEERING
#==============================
def clean_data(df):
    df["GrossSales"]=df["Quantity"]*df["UnitPrice"]
    df["NetSales"]=df["GrossSales"]*(1-df["Discount"])
    df["Month"]=df["Date"].dt.to_period('M')
    return df

#==============================

#METRICS CALCULATION

#==============================

def calculate_metrics(df):
    sales_by_category=df.groupby("Category")["NetSales"].sum()
    sales_by_month=df.groupby("Month")["NetSales"].sum()
    total_revenues=df["NetSales"].sum()
    avg_oder_value=df["NetSales"].mean()
    return sales_by_category,sales_by_month,total_revenues,avg_oder_value

#==============================
#VISUALISATION :
#==============================

def visualise_dahsboard(sales_by_category,monthly_trend):
    fig,axes=plt.subplots(1,2,figsize=(12, 5))
    fig.suptitle("ShopPulse",fontsize=16, fontweight="bold")
    fig.canvas.manager.set_window_title("ShopPulse Analytics")
    #CATEGORY REVENUE
    axes[0].bar(sales_by_category.index,sales_by_category.values)
    axes[0].set_xlabel("Category", color="darkred", fontsize=11)
    axes[0].set_ylabel("Revenue ($)", color="darkred", fontsize=11)
    axes[0].tick_params(axis='x',color="purple",rotation=45)
    axes[0].tick_params(axis='y',color="navy")
    #MONTHLY REVENUE
    axes[1].bar(monthly_trend.index.astype(str),monthly_trend.values)
    axes[1].set_xlabel("Month", color="darkred", fontsize=11)
    axes[1].set_ylabel("Revenue ($)", color="darkred", fontsize=11)
    axes[1].tick_params(axis='x',color="purple",rotation=45)
    axes[1].tick_params(axis='y',color="navy")
    plt.tight_layout()
    plt.show()

#EXCUTION 
if __name__=="__main__":
    df=create_data()
    df=clean_data(df)
    sales_by_category,sales_by_month,total_revenues,avg_oder_value=calculate_metrics(df)
    visualise_dahsboard(sales_by_category,sales_by_month)
    print(f"Total Revenues: {total_revenues}, AVERAGE ORDER VALUE: {avg_oder_value}")