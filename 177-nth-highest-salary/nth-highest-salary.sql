CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  Declare M int;
  set M = N - 1;
  RETURN (
    Select distinct salary from employee order by salary desc limit 1 offset M
  );
END