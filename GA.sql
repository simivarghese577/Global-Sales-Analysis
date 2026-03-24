#--------------------------GOBAL AMAZON SALES ANALYSIS-------------------------------

CREATE DATABASE sales_project;
USE sales_project;

SELECT * FROM sales_data;

SELECT * FROM sales_data LIMIT 5;

#REGION PERFORMANCE
SELECT Region, SUM(`Total Revenue`) AS Revenue
FROM sales_data
GROUP BY Region
ORDER BY Revenue DESC;


#Top 5 Countries by Revenue
SELECT `Country`, SUM(`Total Revenue`) AS Revenue
FROM sales_data
GROUP BY `Country`
ORDER BY Revenue DESC
LIMIT 5;


#MONTHLY TREND
SELECT DATE_FORMAT(`Order Date`, '%Y-%m') AS month,
SUM(`Total Revenue`) AS revenue
FROM sales_data
GROUP BY month
ORDER BY month;


#Orders Count by Region
SELECT `Region`, COUNT(*) AS Total_Orders
FROM sales_data
GROUP BY `Region`
ORDER BY Total_Orders DESC;


#PROFITABILITY
SELECT `Item Type`,
SUM(`Total Profit`)/SUM(`Total Revenue`) AS profit_margin
FROM sales_data
GROUP BY `Item Type`
ORDER BY profit_margin DESC;

#Top 3 Months by Revenue
SELECT DATE_FORMAT(`Order Date`, '%Y-%m') AS Month,
SUM(`Total Revenue`) AS Revenue
FROM sales_data
GROUP BY DATE_FORMAT(`Order Date`, '%Y-%m')
ORDER BY Revenue DESC
LIMIT 3;

#Average Processing Time (Delivery Efficiency) and Highest Single Order Value
SELECT AVG(DATEDIFF(`Ship Date`, `Order Date`)) AS Avg_Delivery_Days,
MAX(`Total Revenue`) AS Highest_Order
FROM sales_data;

#Revenue Contribution % by Region
SELECT Region,SUM(`Total Revenue`) AS Revenue,
(SUM(`Total Revenue`) / (SELECT SUM(`Total Revenue`) FROM sales_data)) * 100 AS Contribution_Percentage
FROM sales_data
GROUP BY `Region`
ORDER BY Contribution_Percentage DESC;


#Rank Products by Revenue (Window Function)
SELECT `Item Type`,SUM(`Total Revenue`) AS Revenue,
RANK() OVER (ORDER BY SUM(`Total Revenue`) DESC) AS Rank_Position
FROM sales_data
GROUP BY `Item Type`;

#Running Total (Cumulative Revenue)
SELECT DATE_FORMAT(`Order Date`, '%Y-%m') AS Month,
SUM(`Total Revenue`) AS Revenue,
SUM(SUM(`Total Revenue`)) OVER (ORDER BY DATE_FORMAT(`Order Date`, '%Y-%m')) AS Running_Total
FROM sales_data
GROUP BY DATE_FORMAT(`Order Date`, '%Y-%m');
