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

3.

```sql
-- check

```
