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
LENGTH(name)	name
6	Angola
5	Benin
8	Botswana
```

# Left

LEFT(s,n) allows you to extract n characters from the start of the string s.

example:   LEFT('Hello world', 4) -> 'Hell'

```sql
SELECT name, LEFT(name, 3)
FROM bbc


Result:

name	LEFT(name, 3)
Angola	Ang
Benin	Ben
Botswana	Bot
```



12. The capital of Sweden is Stockholm. Both words start with the letter 'S'.
    
    Show the name and the capital where the first letters of each match. Don't include countries where the name and the capital are the same word.

```sql
select world.name, world.capital
from world
where LEFT(world.name, 1) = LEFT(world.capital, 1) AND world.name <> world.capital
```

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
