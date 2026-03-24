# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 10:34:41 2026

@author: simiv
"""

#PROJECT 1

#TITLE-----

#------------------------------GLOBAL AMAZON SALES PERFORMANCE ANALYSIS---------------------------------------- 


#IMPORTING LIBARIES
import pandas as pd
import numpy as np

#LOAD THE DATASET
df = pd.read_csv("C:/Users/simiv/Downloads/archive (2)/b9aa812f10e4b60368cff69c6384a210-d24f715d9350d674b0b1bf494d82ccdf81de0647/Amazon sales data.csv")
df

#FIRST 5 LINES
df.head()

#LAST 5 LINES
df.tail()

#DETAILED INFORMATION
df.info()

#DATA CLEANING AND TRANSFROMING

## 1. Converts text dates into date format Required for time-based analysis
df["Order Date"] = pd.to_datetime(df["Order Date"])  
df["Ship Date"] = pd.to_datetime(df["Ship Date"])   


## 2.MISSING VALUES  (Checks for missing values)
df.isnull()
print(df.isnull().sum())

## 3.HANDLE MISSING VALUES PROPERLY (Dropping → removes incomplete rows andFilling → keeps data but replaces missing values)
df["Total Revenue"].mean()
df["Total Revenue"].fillna(df["Total Revenue"].mean(), inplace=True)
df

## 4.REMOVES NEGATIVE OR INVAILD VALUES (Revenue should not be negative so it Removes incorrect entries)
df = df[df["Total Revenue"] > 0]
df

## 5.CREATING USEFUL COLUMNS
df["Profit Margin"] = df["Total Profit"] / df["Total Revenue"]  #Helps measure business efficiency
df                               

df["Processing Days"] = (df["Ship Date"] - df["Order Date"]).dt.days #Shows delivery performance
df



#KEY ANALYSIS

#TOTAL REVENUE AND PROFIT
total_revenue = df["Total Revenue"].sum()
total_profit = df["Total Profit"].sum()

print("Total Revenue:", total_revenue)
print("Total Profit:", total_profit)             #.sum() → adds all values in column and Gives overall business performance


#GROUP BY 
#Top Selling Item Types
item_sales = df.groupby("Item Type")["Total Revenue"].sum().sort_values(ascending=False) #groupby("Item Type") → groups data by product and Then calculates total revenue per product
print(item_sales)        

 #Region-wise Performance
region_sales = df.groupby("Region")["Total Revenue"].sum().sort_values(ascending=False)  #Groups data by region and Shows which region generates more revenue
print(region_sales) 

#Sales Channel Analysis (Online vs Offline)
channel_sales = df.groupby("Sales Channel")["Total Revenue"].sum() #Compares Online vs Offline sales and Shows which channel performs better
print(channel_sales)                  


#AVERAGE DELIVERY DAYS
df["Delivery_Days"] = (df["Ship Date"] - df["Order Date"]).dt.days

avg_delivery = df["Delivery_Days"].mean()

print("Average Delivery Days:", avg_delivery)

#REVENUE CONTRIBUTION
total_revenue = df["Total Revenue"].sum()

region_contribution = (df.groupby("Region")["Total Revenue"].sum() / total_revenue) * 100

print(region_contribution)

#PROFIT MARGIN ANALYSIS
df["Profit_Margin"] = df["Total Profit"] / df["Total Revenue"]

avg_margin = df.groupby("Item Type")["Profit_Margin"].mean().sort_values(ascending=False)

print(avg_margin)


#COMBINED ANALYSIS
summary = {
    "Total Revenue": df["Total Revenue"].sum(),
    "Total Profit": df["Total Profit"].sum(),
    "Avg Delivery Days": df["Delivery_Days"].mean(),
    "Highest Order Value": df["Total Revenue"].max()
}

print(summary)


#DATA VISUALIZATION 
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

#Top Products (Bar Chart)
top_products = df.groupby("Item Type")["Total Revenue"].sum().sort_values(ascending=False)

plt.figure()
top_products.plot(kind="bar")

plt.title("Top Selling Item Types")
plt.xlabel("Item Type")
plt.ylabel("Revenue")

plt.xticks(rotation=45)
plt.show()


#Region-wise Revenue (Seaborn)
region_sales = df.groupby("Region")["Total Revenue"].sum().reset_index()

plt.figure()
sns.barplot(data=region_sales, x="Region", y="Total Revenue")

plt.title("Revenue by Region")
plt.xticks(rotation=45)

plt.show()


#Monthly Sales Trend (Line Chart)
df["Month"] = df["Order Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Total Revenue"].sum()

plt.figure()
monthly_sales.plot(marker="*")

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.show()


#Sales Channel (Pie Chart)
channel_sales = df.groupby("Sales Channel")["Total Revenue"].sum()

plt.figure()
channel_sales.plot(kind="pie", autopct='%1.1f%%')

plt.title("Sales Channel Distribution")

plt.show()


#Profit vs Revenue (Scatter Plot)
plt.figure()
sns.scatterplot(data=df, x="Total Revenue", y="Total Profit")

plt.title("Revenue vs Profit")

plt.show()


#Delivery Time Distribution
plt.figure()
sns.histplot(df["Delivery_Days"], bins=20)

plt.title("Delivery Time Distribution")

plt.show()

