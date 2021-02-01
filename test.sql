create database PythonTest

use PythonTest

select @@SERVERNAME

create table TestTable(TID int, Name nvarchar(10))

insert into TestTable(TID, Name)
values (101, 'TestTable')

select * from TestTable