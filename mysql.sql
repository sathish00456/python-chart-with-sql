create database st;
use st;
create table emp (empid int primary key auto_increment, empname varchar(20),place varchar(30),salary int);
insert into emp (empid,empname,place,salary) values (8,'balaji','chennai',4000),(9,'jeyakrishna','ambur',5000),(10,'salman','thiruvallur',8000);
select * from emp;
select empname,count(empname),count(salary) from emp group by salary,empname having salary=30000;