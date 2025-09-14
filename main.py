import pandas as pd

df = pd.read_csv("Coffe_sales.csv")

# =======================
# 1. Basic Analysis     #
# =======================
print(df.head())

print(df.info())

print(df.describe())

print(df.isnull().sum())

# =======================
# 2. Common Q/A         #
# =======================

# most popular coffee
coffee_count = df['coffee_name'].value_counts()
print(coffee_count)
print("The most popular coffee is: ",coffee_count.idxmax())

# time of day, that brings most money
sales_by_time = df.groupby('Time_of_Day').sum()['money']
print(sales_by_time)
print("Time of the day that brings most money is: ",sales_by_time.idxmax())

# kind of payment people prefer
prefer_payment = df['cash_type'].value_counts()
print(prefer_payment)
print("Most people prefer payment by: ",prefer_payment.idxmax())

# busiest day of the week
busiest_day = df['Weekday'].value_counts()
print(busiest_day)
print("The most busiest day of the week is: ", busiest_day.idxmax())

# busiest month of the year
busiest_year = df['Month_name'].value_counts()
print(busiest_year)
print("The most busiest month of the year is: ",busiest_year.idxmax())