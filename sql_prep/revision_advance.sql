-- Advanced Q1: Find the top 3 products by sales (or top 3 employees by salary) overall, 
-- and then specifically within each category/department.

--top 3 sales across categories
select top 3 product_id, 
category, 
sum(sales) total_sales
from orders
GROUP BY product_id, category
order by sum(sales) desc

--within categories

with agg as 
(select 
product_id, 
category, 
sum(sales) total_sales
from orders
GROUP BY product_id, category)
select * from
(select * ,
ROW_NUMBER() over(PARTITION BY category order by total_sales desc) rnk
from agg)a
where rnk <4



select order_id, product_id, category, sales from orders

-- Advanced Q2: How to calculate Year-over-Year (YoY) sales growth percentage using LEAD and LAG 
-- -- Advanced Q3: How to calculate a cumulative sum (running total), and how to calculate a moving "rolling 3-month" sa
-- -- Advanced Q4: How to pivot year-wise category sales from rows into distinct columns (e.g., separate columns for Furniture Sales, Technology Sales, etc., 
-- -- Advanced Q5: (Join outputs recap—instructor refers to his dedicated video for this
-- -- d Complex SQL Problems (From Real Big Tech In
-- -- Hard Problem 1 (Asked at Meta): "Workaholic Employees." Write a query to flag employees who either worked >8 hours for at least 3 days a week, OR worked >10 hours for at least 2 da
-- -- Hard Problem 2 (Asked at LinkedIn): "Malware Detection." Find out how many malwares each software detected in its latest run, and calculate the difference between the latest run and the second-l
-- -- Hard Problem 3: "User Session Activity." Given a log of user events, identify and group individual "sessions" based on the rule that a gap of >30 minutes between events starts a brand ne
-- -- Hard Problem 4: "Project Budget." Forecast salaries based on a project's duration (in days) to calculate if the assigned employees' combined salaries will fall 'Within Budget' or 'Ove
-- -- Hard Problem 5: "Employees' Current Salary." Compute the final current salary of an employee by sequentially applying a list of multi-staged percentage promotions (using Recurs