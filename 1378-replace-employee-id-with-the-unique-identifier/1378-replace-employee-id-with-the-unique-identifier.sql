# Write your MySQL query statement below
select uni.unique_id, emp.name from Employees as emp
left join EmployeeUNI as uni 
on uni.id = emp.id;