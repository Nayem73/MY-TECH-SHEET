# SQL

1. Primary key = Not NULL + UNIQUE

![](assets/2024-01-08-11-32-22-image.png)



2. if somebody didn't enter a major, instead of that field being left as NULL, it will be filled `undecided` by default because of `default` keyword

![](assets/2024-01-08-11-36-38-image.png)



3. Auto increment the primary key instead of manually putting it in everytime creating a row.

![](assets/2024-01-08-11-39-10-image.png)



4. update a specific column with update keyword:

![](assets/2024-01-08-11-42-21-image.png)

![](assets/2024-01-08-11-45-24-image.png)

![](assets/2024-01-08-11-46-36-image.png)



* If I don't use a condition whith `where` keyword, all the rows will be affected:

![](assets/2024-01-08-11-47-45-image.png)



5. Delete Row

![](assets/2024-01-08-11-48-44-image.png)

![](assets/2024-01-08-11-49-42-image.png)

* if we don't use the `Where` clause, all the rows/entries will be deleted but the table will be still there:

![](assets/2024-01-08-11-51-11-image.png)



# Query

1. ![](assets/2024-01-08-12-06-48-image.png)

2.   ![](assets/2024-01-08-12-07-37-image.png)

3. ![](assets/2024-01-08-12-08-21-image.png)

4. Names are in sorted order

![](assets/2024-01-08-12-09-16-image.png)

5. sort names in desc order

![](assets/2024-01-08-12-10-06-image.png)

6. result would show in terms of sorted student id

![](assets/2024-01-08-12-11-02-image.png)

![](assets/2024-01-08-12-11-32-image.png)

![](assets/2024-01-08-12-13-05-image.png)

7. Limit the result shown:

![](assets/2024-01-08-12-13-44-image.png)

![](assets/2024-01-08-12-14-06-image.png)



# Query with filtering

1. ![](assets/2024-01-08-12-15-23-image.png)

2. ![](assets/2024-01-08-12-15-53-image.png)

3. ![](assets/2024-01-08-12-16-24-image.png)

4. all student with major not equal to chemistry:

![](assets/2024-01-08-12-17-22-image.png)

![](assets/2024-01-08-12-18-00-image.png)

* 

* 

* 

* ***IN keyword:***

![](assets/2024-01-08-12-19-44-image.png)

![](assets/2024-01-08-12-20-37-image.png)

![](assets/2024-01-08-12-21-03-image.png)



# Company database (Relational Database) :

composite key: multiple primary key is necessary because. For example, only marks may not uniquely identify each row, you might need a username too.

or,

emp_id sold 500,000 worth of product to client_id. in this case, we need emp_id and client_id both as primary key because both needs to match with each other for their sales info.(how much emp x sold to client y)



1. ![](assets/2024-01-08-14-50-06-image.png)

2. ![](assets/2024-01-08-14-51-03-image.png)

3. ![](assets/2024-01-08-14-51-57-image.png)

4. ![](assets/2024-01-08-14-53-09-image.png)

5. ![](assets/2024-01-08-14-53-43-image.png)

6. ![](assets/2024-01-08-14-54-31-image.png)

7. Distinct Keyword

![](assets/2024-01-08-14-57-06-image.png)

![](assets/2024-01-08-14-57-33-image.png)





# SQL Functions

1. Count()

![](assets/2024-01-08-14-59-11-image.png)

![](assets/2024-01-08-14-59-58-image.png)

![](assets/2024-01-08-15-01-34-image.png)



2. AVG()

![](assets/2024-01-08-15-03-06-image.png)

![](assets/2024-01-08-15-03-32-image.png)



3. SUM()

![](assets/2024-01-08-15-04-15-image.png)



# Aggregation:

* And aggregation is basically where we can use the above functions and we can display the data that we get back in a more helpful way.

![](assets/2024-01-08-15-06-37-image.png)

![](assets/2024-01-08-15-06-59-image.png)

![](assets/2024-01-08-15-07-21-image.png)

![](assets/2024-01-08-15-08-50-image.png)



* How much each client spent:

![](assets/2024-01-08-15-09-43-image.png)



# WildCards

* in the example below, % means there wil be any number of characters and it needs to match with LLC at the end of the string.

![](assets/2024-01-08-17-25-34-image.png)

* this time, it will match any substring that matches with Label

![](assets/2024-01-08-17-27-38-image.png)

* here, 4 underscore means 4 characters, we did it for year

![](assets/2024-01-08-18-04-04-image.png)



# Union


