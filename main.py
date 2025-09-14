import pandas as pd
import matplotlib.pyplot as plt

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

# ===============================
# 3. Visualization of Data      #
# ===============================

# most popular coffee plot
coffee_count = df['coffee_name'].value_counts()
plt.figure(figsize=(8,5))
coffee_count.plot(kind="bar",color="orange")
plt.title("Most Popular Coffee")
plt.xlabel("Coffee type")
plt.xticks(rotation=55)
plt.ylabel("Number of purchase")
for i,values in enumerate(coffee_count):
    plt.text(i,values+(0.01*values),str(values),ha="center")
plt.show()

# time of day, that brings most money plot
sales_by_time = df.groupby('Time_of_Day').sum()['money']
plt.figure(figsize=(8,5))
sales_by_time.plot(kind="bar",color="orange")
plt.title("Peak sales hour")
plt.xlabel("Time of day")
plt.xticks(rotation=55)
plt.ylabel("Sales")
for i,values in enumerate(sales_by_time):
    plt.text(i,values+(0.01*values),str(values),ha="center")
plt.show()

# busiest day of the week plot
busiest_day = df['Weekday'].value_counts()
plt.figure(figsize=(8,5))
busiest_day.plot(kind="bar",color="orange")
plt.title("Busiest day of week")
plt.xlabel("Days")
plt.ylabel("Sales")
for i,values in enumerate (busiest_day):
    plt.text(i,values+(0.01*values),str(values),ha="center")
plt.show()

 # busiest month of the year plot
busiest_month = df['Month_name'].value_counts()
plt.figure(figsize=(8,5))
busiest_month.plot(kind="bar",color="orange")
plt.title("Busiest month of year")
plt.xlabel("Month")
plt.ylabel("Sales")
for i,values in enumerate (busiest_month):
    plt.text(i,values+(0.01*values),str(values),ha="center")
plt.show()
