import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#=================================
#    DATA CREATION
#=================================
np.random.seed(33)
rows_number=1000

categories = ['Electronics', 'Apparel', 'Home & Kitchen', 'Books', 'Beauty']
payments = ['Credit Card', 'PayPal', 'Debit Card', 'Cash']

data={
    "Transaction_id":[f"TN-{1000+i}" for i in range(rows_number)],
    "Date":pd.date_range(start='2026-01-01',end='2026-12-31',periods=rows_number),
    "Category":np.random.choice(categories,rows_number,p=[0.3,0.2,0.1,0.3,0.1]),
    "Quantity":np.random.randint(1,6,rows_number),
    "Unit Price":np.random.uniform(12.0,300.0,rows_number),
    "Discount":np.where(np.random.rand(rows_number)>0.75,0.15,0.0),
    "Payment Method":np.random.choice(payments,rows_number,p=[0.3,0.2,0.2,0.3])}

df=pd.DataFrame(data)
df.to_csv("data.csv")
print("File Saved Sucessfully !")


