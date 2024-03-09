1. first real:

```sql
create database world;
use world;
create table student(
    id int,
    name varchar(20),
    dept varchar(20),
    primary key(id)
);

insert into student values(1, "Minhaz", "CSE");
insert into student values(2, "Arafat", "EEE");
insert into student(id, name) values(3, 'Rifat');

INSERT INTO table_name (column1, column2, column3)
VALUES ('value1', 'value2', 'value3'),
VALUES ('value1', 'value2', 'value3');


select * from student
where
student.name = "Rifat";

alter table student add gpa decimal(3,2);
alter table student add money DECIMAL(4,2);
alter table student add foreign key(teacher_id) REFERENCES teacher(teacher_id) ON DELETE SET NULL;

ALTER TABLE student CHANGE dob birth_day DATE; -- rename a column name

ALTER TABLE student DROP COLUMN gpa; -- Delete a column

select * from student;

update student
set gpa = 3.24
where student.id = 1;


delete from student  -- delete a row
where student.id = 3;


SELECT DISTINCT student.sex
FROM student;
```

# Equivalent Nested Queries for instead of Join

- These will produce same results 

```sql
select orders.customer_name
from orders
where orders.product_id IN (
    select products.product_id
    FROM products
    where products.product_name = 'Laptop'
);
select orders.customer_name
from orders
join products
where products.product_id = orders.product_id AND products.product_name = 'Laptop';
```

- These will also produce the same results:

```sql
select employee.name
from employee
where employee.emp_id IN (
    select branch.mgr_id
    from branch
);

select employee.name, branch.branch_name
from employee
join branch
ON employee.emp_id = branch.mgr_id;
```

-------

- If I do this, error! because foregin key with emp_id 111 does not exist!

```sql
insert into Branch values(5, "Buffalo", 111, "1998-02-01");
```

- find first 5 people

```sql
select * from employee
LIMIT 5
```

- find first 5 best salary people

```sql
select * from employee
order by employee.salary desc
LIMIT 5
```

- find last 5 people

```sql
SELECT * FROM employee
ORDER BY id DESC
LIMIT 5;
```

- find last 5 people except the last 2 people

```sql
select * from employee
order by employee.id desc
limit 5 offset 2;
```

- find the first 5 after 2 people

```sql
select * from employee
LIMIT 5 OFFSET 2;
```

- find second highest salary

```sql
select employee.employee_id, employee.first_name, employee.dept_Id
from employee order by employee.salary desc
limit 1 offset 1;
```

- List the First 50% Rows

```sql
SELECT * FROM table_name
LIMIT (
    SELECT ROUND(COUNT(*) * 0.5)
    FROM table_name
);
```

# Aggregate

- how many type of expertise are there and list these expertise name

```sql
select expertise, count(expertise)
from employee group by expertise;
```

- Sure, I can help you learn about aggregate functions in SQL. Aggregate functions are special functions that perform calculations on a group of rows and return a single value. They are often used with the GROUP BY clause to summarize data or perform statistical analysis. Some of the most common aggregate functions are:
  
  - **SUM ()**: returns the total sum of a numeric column.
  - **COUNT ()**: returns the number of rows or non-null values in a column.
  - **AVG ()**: returns the average value of a numeric column.
  - **MIN ()**: returns the minimum value of a column.
  - **MAX ()**: returns the maximum value of a column.
  
  To demonstrate how these functions work, let’s create a sample table called `sales` with the following data:
  
  | id  | product | quantity | price |
  | --- | ------- | -------- | ----- |
  | 1   | A       | 10       | 100   |
  | 2   | B       | 20       | 200   |
  | 3   | C       | 30       | 300   |
  | 4   | A       | 15       | 150   |
  | 5   | B       | 25       | 250   |
  
  We can use the following SQL statement to create and populate the table:
  
  ```sql
  CREATE TABLE sales (
    id INT PRIMARY KEY,
    product VARCHAR(10),
    quantity INT,
    price INT
  );
  
  INSERT INTO sales VALUES
  (1, 'A', 10, 100),
  (2, 'B', 20, 200),
  (3, 'C', 30, 300),
  (4, 'A', 15, 150),
  (5, 'B', 25, 250);
  ```
  
  Now, let’s see some examples of using aggregate functions on this table.
  
  - To find the total revenue of all sales, we can use the SUM () function on the price column:
  
  ```sql
  SELECT SUM(price) AS total_revenue FROM sales;
  ```
  
  The result is:
  
  | total_revenue |
  | ------------- |
  | 1000          |
  
  - To find the number of products sold, we can use the COUNT () function on the product column:
  
  ```sql
  SELECT COUNT(product) AS total_products FROM sales;
  ```
  
  The result is:
  
  | total_products |
  | -------------- |
  | 5              |
  
  ```sql
  select product, count(product)
  from sales
  group by product;
  ```
  
  the result is:
  
  | product | count(product) |
  | ------- | -------------- |
  | A       | 2              |
  | B       | 2              |
  | C       | 1              |
  
  - To find the average price of all products, we can use the AVG () function on the price column:
  
  ```sql
  SELECT AVG(price) AS average_price FROM sales;
  ```
  
  The result is:
  
  | average_price |
  | ------------- |
  | 200           |
  
  - To find the lowest price of any product, we can use the MIN () function on the price column:
  
  ```sql
  SELECT MIN(price) AS lowest_price FROM sales;
  ```
  
  The result is:
  
  | lowest_price |
  | ------------ |
  | 100          |
  
  - To find the highest price of any product, we can use the MAX () function on the price column:
  
  ```sql
  SELECT MAX(price) AS highest_price FROM sales;
  ```
  
  The result is:
  
  | highest_price |
  | ------------- |
  | 300           |
  
  These are some basic examples of using aggregate functions in SQL. You can learn more about them from these sources: [SQL Aggregate Functions - SQL Tutorial](https://www.sqltutorial.org/sql-aggregate-functions/), [SQL Aggregate Functions: A Comprehensive Guide for Beginners](https://learnsql.com/blog/aggregate-functions/), [SQL Aggregate Functions: Explore 5 Types of Functions - Simplilearn](https://www.simplilearn.com/tutorials/sql-tutorial/sql-aggregate-functions).
  
  I hope this helps you understand aggregate functions in SQL. If you have any questions, feel free to ask me. 😊

----

----

Hello, this is Copilot. I can help you with your SQL queries. 😊

To delete a database in MySQL, you can use the DROP DATABASE statement. The syntax is as follows:

```sql
DROP DATABASE database_name;
```

This statement will remove the database and all its tables, views, triggers, and stored procedures. However, you need to be careful before dropping a database, as you will lose all the data and information stored in it.

For example, if you want to delete a database named testDB, you can use this query:

```sql
DROP DATABASE testDB;
```

You can also use the IF EXISTS option to avoid getting an error if the database does not exist. For example:

```sql
DROP DATABASE IF EXISTS testDB;
```

This query will delete the testDB database if it exists, or do nothing otherwise.

[For more information and examples on how to delete a database in MySQL, you can check out these web pages](https://www.w3schools.com/mysql/mysql_drop_db.asp)[1](https://www.w3schools.com/mysql/mysql_drop_db.asp)[2](https://stackoverflow.com/questions/1082130/how-do-i-remove-a-mysql-database)[3](https://www.mysqltutorial.net/mysql-drop-database/)[4](https://www.slingacademy.com/article/ways-to-drop-database-mysql-8/).

I hope this helps. If you have any other questions, please let me know. Have a nice day! 👋





# Duplicate Rows

> find duplicate rows

Sure, here is a general SQL query to find duplicate rows in a table. Please replace `table_name` and `column1`, `column2`, etc. with your actual table name and column names.

```sql
SELECT column1, column2, ..., COUNT(*)
FROM table_name
GROUP BY column1, column2, ...
HAVING COUNT(*) > 1;
```

This query groups the table by all its columns and then uses the `HAVING` clause to filter out the groups that appear more than once, which are the duplicate rows. If you have specific columns you want to check for duplicates, you can replace `column1, column2, ...` with those column names. If you want to check the entire row for duplicates, you should include all columns in the `GROUP BY` clause.

Please note that this query will only show you the duplicated rows. If you want to delete duplicates, you would need a different approach, and you should be very careful as it involves deleting data from your table. Always make sure to backup your data before running such queries.



> Delete duplicate rows



Deleting duplicate rows in SQL can be a bit tricky because it involves removing data from your table. Here is a general approach to do it:

1. First, create a temporary table with the distinct records from the original table:

```sql
CREATE TABLE temp_table AS
SELECT DISTINCT *
FROM original_table;
```

2. Then, delete everything from the original table:

```sql
DELETE FROM original_table;
```

3. After that, insert the distinct records back into the original table from the temporary table:

```sql
INSERT INTO original_table
SELECT * FROM temp_table;
```

4. Finally, drop the temporary table as it’s no longer needed:

```sql
DROP TABLE temp_table;
```

Please replace `original_table` with your actual table name.

**Important:** Always make sure to backup your data before running such queries. This is a general approach and might not work for all scenarios, especially when you have constraints or dependencies on your table. It’s always a good idea to test the queries on a small set of data or a dummy table before running them on the actual table. If your table is large, there might be more efficient ways to delete duplicates. If you’re unsure, it’s best to ask for help from a database administrator or a more experienced colleague.
