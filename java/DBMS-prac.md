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

select * from student
where
student.name = "Rifat";

alter table student add gpa decimal(3,2);
select * from student;

update student
set gpa = 3.24
where student.id = 'Minhaz';
```

2. second real:
