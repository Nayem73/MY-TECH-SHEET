# [SELECT basics - SQLZoo](https://www.sqlzoo.net/wiki/SELECT_basics)

1.

```sql
SELECT world.population
FROM world
WHERE world.name = 'Germany';
```

2.

```sql
-- check original
SELECT world.name, world.population
FROM world
WHERE world.name IN (
  SELECT world.name
  FROM world
  where world.name = 'Sweden' OR world.name = 'Norway' OR world.name = 'Denmark'
);
```

# Where basic

1. wow this works! `population/area`

```sql
SELECT name, population/area, 0, 2*2 FROM bbc
  WHERE area > 5000000
```

# Correct Basic Mistakes

- Mistake1:

```sql
select world.name, world.population
from world IN world.name = (
  'France', 'Germany', 'Italy'
);
```

- Correct1:

```sql
select world.name, world.population
from world
where world.name IN (
  'France', 'Germany', 'Italy'
);
```

# Round

- Show the `name` and `population` in millions and the GDP in billions for the countries of the `continent` 'South America'. Use the [ROUND](https://www.sqlzoo.net/wiki/ROUND "ROUND") function to show the values to two decimal places.
- `ROUND(7253.86, 0)    ->  7254
  ROUND(7253.86, 1)    ->  7253.9
  ROUND(7253.86,-3)    ->  7000`

```sql
select world.name, ROUND(world.population/1000000.0, 2) as population, ROUND(world.gdp/1000000000.0, 2) as GDP
from world
where world.continent = 'South America'
```

- ```sql
  what is the difference between these two? explain with example:
  select world.name, round(world.gdp/world.population, 3)
  from world
  where world.gdp >= 1000000000000
  
  and the other one:
  
  select world.name, round(world.gdp/world.population, -3)
  from world
  where world.gdp >= 1000000000000
  ```

The difference between these two SQL queries lies in the `ROUND` function’s second parameter, which specifies the number of decimal places to round to.

1. `ROUND(world.gdp/world.population, 3)`: This rounds the result of `world.gdp/world.population` to 3 decimal places. For example, if `world.gdp/world.population` is `1234.56789`, it will be rounded to `1234.568`.

2. `ROUND(world.gdp/world.population, -3)`: This rounds the result of `world.gdp/world.population` to the nearest 1000 (because -3 rounds to the nearest 10^-3 = 1/1000). For example, if `world.gdp/world.population` is `1234567.89`, it will be rounded to `1235000`.

So, the first query gives a more precise per capita GDP, while the second query gives a less precise per capita GDP rounded to the nearest thousand. Both queries only consider countries with a GDP of at least 1 trillion (1,000,000,000,000).

# String Length

Greece has capital Athens.

Each of the strings 'Greece', and 'Athens' has 6 characters.

Show the name and capital where the name and the capital have the same number of characters.

```sql
select world.name, world.capital
from world
where length(world.name) = length(world.capital)
```

```sql
SELECT LENGTH(name), name
FROM bbc

Result:
LENGTH(name)    name
6    Angola
5    Benin
8    Botswana
```

# Left

LEFT(s,n) allows you to extract n characters from the start of the string s.

example:   LEFT('Hello world', 4) -> 'Hell'

```sql
SELECT name, LEFT(name, 3)
FROM bbc


Result:

name    LEFT(name, 3)
Angola    Ang
Benin    Ben
Botswana    Bot
```

12. The capital of Sweden is Stockholm. Both words start with the letter 'S'.
    
    Show the name and the capital where the first letters of each match. Don't include countries where the name and the capital are the same word.

```sql
select world.name, world.capital
from world
where LEFT(world.name, 1) = LEFT(world.capital, 1) AND world.name <> world.capital
```

# CONCAT

CONCAT allows you to stick two or more strings together.

This operation is concatenation.

   CONCAT(s1, s2 ...)   

1. In this example you put the region and the name together for each country.

```sql
SELECT CONCAT(region,name)
FROM bbc


-- output:
CONCAT(region..
AfricaAngola
AfricaBenin
AfricaBotswana
AfricaBurkina Faso
```

# Substring

`SUBSTRING('Hello world', 2, 3) -> 'ell'`

2 = from second character.

3 = length 3 from that second character

```sql
SELECT name, SUBSTRING(name, 2, 5)
FROM bbc

-- output

name    SUBSTRING(nam..
Angola    ngola
Benin    enin
Botswana    otswa
Burkina Faso    urkin
Burundi    urund 
```

# Trim

TRIM(s) returns the string with leading and trailing spaces removed.

`   TRIM('Hello world  ') -> 'Hello world'`

```sql
SELECT name, TRIM(name)
FROM bbc
```

# ------- Mathematical -----

# Mod

`MOD(27,2) ->  1
 MOD(27,10) ->  7`

```sql
SELECT MOD(yr,10), yr, city
FROM games
```

# Ceil

`CEIL(2.7)  ->  3
 CEIL(-2.7) -> -2`

# floor

`  FLOOR(2.7) ->  2
  FLOOR(-2.7) -> -3`

# Not LIKE

13. ```sql
    select world.name
    from world
    where world.name NOT LIKE '% %' AND world.name LIKE '%a%' AND
    world.name LIKE '%e%' AND
    world.name LIKE '%i%' AND
    world.name LIKE '%o%' AND
    world.name LIKE '%u%';
    ```

# NOT IN

The `NOT IN` keyword in SQL is used to exclude certain values. Here’s an example:

Let’s say we have a table called `Students` with a column `Name`, and we want to find all students except ‘John’, ‘Jane’, and ‘Jim’. We would write:

```sql
SELECT * 
FROM Students
WHERE Name NOT IN ('John', 'Jane', 'Jim');
```

This will return all students whose names are not ‘John’, ‘Jane’, or ‘Jim’.

I hope this helps! Let me know if you have any other questions. 😊

--------

# Nested Query (Nested Select)

2. Find the countries in the same continent as Bhutan

```sql
select world.name
from world
where world.continent IN(
  select world.continent
  from world
  where world.name = 'Bhutan'
);
```

3. I did a different task when I was trying 3.
- this query is comparing the population of each country to 5 times the average area of all countries: (here, note that when using AVG, I need to use SELECt as well)

```sql
select world.name
from world
where world.population IN(
  select world.population
  from world
  where world.population > 5* (select AVG(world.area) from world)

);
```

3. This is the original number 3 question: Show the countries where the population is greater than 5 times the average for its region

```sql
select bbc.name
from bbc
where bbc.population > 5 * (
  select AVG(inner_bbc.population)
  from bbc as inner_bbc
  where inner_bbc.region = bbc.region
);
```

# SELECT within SELECT Tutorial - 2

1. List each country **name** where the **population** is larger than that of 'Russia'.

```sql
select world.name
from world
where world.population > (
  select world_inner.population
  from world as world_inner
  where world_inner.name = 'Russia'
);
```

4. Which country has a population that is more than United Kingdom but less than Germany? Show the name and the population.

```sql
select world.name, world.population
from world
where world.population > (
  select world.population
  from world
  where world.name = 'United Kingdom'
) AND world.population < (
  select world.population
  from world
  where world.name = 'Germany'
);
```

5. Germany (population 80 million) has the largest population of the countries in Europe. Austria (population 8.5 million) has 11% of the population of Germany.
   
   Show the name and the population of each country in Europe. Show the population as a percentage of the population of Germany.
   
   The format should be *Name, Percentage* for example:
   
   | name    | percentage |
   | ------- | ---------- |
   | Albania | 3%         |
   | Andorra | 0%         |
   | Austria | 11%        |
   | ...     | ...        |
- wow, ***<u>Alhamdulillah, new thing learnt</u>*** ([sqlzoo select in select 5 - YouTube](https://youtu.be/lCbLvHUNBG4))

```sql
select world.name, concat(round(world.population/(
  select world.population
  from world
  where world.name = 'Germany'
) * 100, 0), '%') as percentage
from world
where world.continent = 'Europe'

-- output:
name    concat(round(..
Albania    3%
Andorra    0%
Austria    11%
Belarus    11%
Belgium    14%
```

6. Which countries have a GDP greater than every country in Europe? [Give the **name** only.] (Some countries may have NULL gdp values)
- below will return error because: `Error: Subquery returns more than 1 row`

- ```sql
  select world.name
  from world
  where world.gdp > (
    select world.gdp
    from world
    where world.continent = 'Europe'
  );
  ```

- for comparison operators (=, >, <, etc) I can not return more than one row. To return more than one row, I need to use  `IN` keyword or `ALL` keyword: this is a correct code:

- ```sql
  select world.name
  from world
  where world.gdp > ALL(
    select world.gdp
    from world
    where world.continent = 'Europe'
  );
  ```

- Also, I can use MAX or AVG etc so that the subquery returns only one row:

```sql
select world.name
from world
where world.gdp > (
  select MAX(world.gdp)
  from world
  where world.continent = 'Europe'
);
```

# [SUM and COUNT - SQLZoo](https://www.sqlzoo.net/wiki/SUM_and_COUNT)

1. Show the total **population** of the world.

```sql
select sum(world.population)
from world;
```

2. List all the continents - just once each.

```sql
select DISTINCT world.continent
from world
```

3. Give the total GDP of Africa

```sql
select sum(world.gdp)
from world
where world.continent = 'Africa'
```

5. What is the total **population** of ('Estonia', 'Latvia', 'Lithuania')

```sql
select sum(world.population)
from world
where world.name IN (
'Estonia', 'Latvia', 'Lithuania'
);
```

# [Using GROUP BY and HAVING. - SQLZoo](https://www.sqlzoo.net/wiki/Using_GROUP_BY_and_HAVING.)

1. For each continent show the number of countries

```sql
select world.continent, count(world.name)
from world
group by world.continent; 


-- output:
continent    count(world.n..
Africa    54
Asia    47
Europe    44
Insular Oceania    14
North America    23
South America    12
```

2. For each continent show the total population:

```sql
select world.continent, sum(world.population)
from world
group by world.continent; 


-- output:
continent    sum(world.pop..
Africa    1364367473
Asia    4635206388
Europe    765378695
Insular Oceania    46247099
North America    593576652
South America    425724580
```

3. Rules for using `WHERE` and `GROUP BY` together:  The WHERE filter takes place before the aggregating function. 
   
   - For each relevant continent show the number of countries that has a population of at least 200000000.

```sql
select world.continent, count(world.name)
from world
where world.population >= 200000000
group by world.continent 


-- output
continent    count(world.n..
Africa    1
Asia    4
North America    1
South America    1
```

### Having

- The HAVING clause is tested after the GROUP BY. You can test the aggregated values with a HAVING clause.
4. Show the total population of those continents with a total population of at least half a billion (500000000)

```sql
select world.continent, sum(world.population)
from world
group by world.continent
having sum(world.population) >= 500000000
```

### *<u>Now, see the differences why we used `where` clause in the previous  code and why we used `having` clause in this code.</u>*
