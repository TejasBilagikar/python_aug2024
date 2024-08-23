create table employees(id int primary key auto_increment, name varchar(50) not null, designation varchar(40) not null, technology varchar(30) not null, phone_num bigint unique, commission int, salary float default 0, years_of_exp int);

select * from employees;

insert into employees(name, designation, technology, phone_num, commission, salary, years_of_exp) values('ganesh', 'human resources', 'vlsi', 3654789512, 10000 , 50000, 9);

insert into employees(name, designation, technology, phone_num, commission, salary, years_of_exp) values('anirudh', 'team lead', 'sql', 6544789512, 9000, 44000, 7);

insert into employees(name, designation, technology, phone_num, commission, salary, years_of_exp) values('sohail', 'product manager', 'mba', 5644789512, 9000, 35000, 5);

insert into employees(name, designation, technology, phone_num, commission, salary, years_of_exp) values('prasanna', 'design manager', 'architecture', 3254789512, 9000, 35000, 5);

insert into employees(name, designation, technology, phone_num, commission, salary, years_of_exp) values('rohan', 'designer', 'graphic design', 7843789512, 8000, 35000, 3);

insert into employees(name, designation, technology, phone_num, commission, salary, years_of_exp) values('kiran', 'designer', 'visual design', 5648789512, 7000, 34000, 5);

insert into employees(name, designation, technology, phone_num, salary, years_of_exp) values('manoj', 'programer', 'python', 7589789512, 32000, 7);

insert into employees(name, designation, technology, phone_num, salary, years_of_exp) values('shridhar', 'secretory', 'tech', 3564789512, 35000, 6);

insert into employees(name, designation, technology, phone_num, salary, years_of_exp) values('ramu', 'designer', 'product designer', 69694789512, 32000.00, 2);

update employees set salary = 50000 where id = 1;

delete from employees where id = 10;

select count(*) as Num_Of_Employee from employees;

select count(distinct salary) as Num_Of_Emps from employees;

-- select dept, SUM(empsal) as TOTAL_SAL from employee group by dept;
select SUM(salary) as total_salary from employees;
 
 -- select 'Telecom' dept, MIN(empsal) from employee where dept='Telecom'
 select MIN(salary) from employees;
 
  select MAX(salary) from employees;

