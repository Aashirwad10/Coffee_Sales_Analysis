import pandas as pd

df = pd.read_csv("Coffe_sales.csv")

# =======================
# 1. Basic Analysis     #
# =======================
print(df.head())

print(df.info())

print(df.describe())

print(df.isnull().sum())