-- Part 1: The Top 10 Most Common SQL Questions:

-- Question 1: How to find duplicate records in a given table? (Using GROUP BY a

select count(*) dup_count,
emp_id 
from employee
group by emp_id
having count(*) >1;

-- Question 2: How to delete the duplicates you found? (Using CTEs and ROW func)
with dup as
(select *,
ROW_NUMBER() over(PARTITION BY emp_id ORDER BY emp_id) as rn
from employee
)
delete dup where rn > 1

-- Question 3: What is the difference between UNION and UNIONALL

select manager_id from employee
UNION
select manager_id from employee

-- Question 4: What is the difference between RANK, ROW_NUMBER, and Dense_rank , rank

select *,
ROW_NUMBER() over(order by salary desc) as rn,
RANK() over(order by salary desc) as rnk,
DENSE_RANK() over(order by salary desc) as drnk
FROM
employee;

select *,
ROW_NUMBER() over(PARTITION by dept_id order by salary desc) as rn,
RANK() over(PARTITION by dept_id order by salary desc) as rnk,
DENSE_RANK() over(PARTITION by dept_id order by salary desc) as drnk
FROM
employee

-- Question 5: How to find employees who are not present in the department table? (Solved using both Subqueries and LEFT JOIN )
select * from employee e
left join dept d
on e.dept_id = d.dep_id
where d.dep_id is null


select * 
from employee
where dept_id not in (select dep_id from dept);

-- Question 6: How to find the employee with the second highest salary in each d
select * from
(select *,
DENSE_RANK() OVER(partition by dept_id order by salary desc) drnk
from employee) a
where drnk = 2;

-- Question 7: How to find all transactions by a specific customer, and how do you handle case-insensitivity in

select * from orders

-- Question 8: How to find employees whose salary is greater than their manager
select * 
from employee e
join employee m
on m.emp_id = e.manager_id
where e.salary > m.salary

select * 
from employee e
join employee m
on e.emp_id = m.manager_id
where e.salary > m.salary


-- Question 9: What is the difference between LEFT JOIN, INNER JOIN, RIGHT JOIN, and FULL O


select * from TableA
select * from TableB

select * from TableA
inner join TableB
on TableA.col1 = TableB.col1

select * from TableA
left join TableB
on TableA.col1 = TableB.col1

select * from TableA
right join TableB
on TableA.col1 = TableB.col1

select * from TableA
full outer join TableB
on TableA.col1 = TableB.col1

-- Question 10: How to swap values in a single column without using multiple update statements? (e.g., fixing a mistake by swapping 'Male' to 'Female' and vice versa using CASE WHEN).