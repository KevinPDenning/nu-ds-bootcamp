SELECT e.emp_no, e.last_name, e.first_name, e.sex, s.salary
FROM employees AS e
JOIN salaries as s
ON e.emp_no = s.emp_no;

SELECT * FROM salaries LIMIT 20;
SELECT * FROM employees LIMIT 20;


SELECT first_name, last_name, hire_date
FROM employees
WHERE hire_date >= '1986-01-01' 
AND hire_date <= '1986-12-31';


SELECT dmgr.dept_no, dpt.dept_name, e.emp_no, e.last_name, e.first_name
FROM dept_manager AS dmgr
JOIN departments AS dpt
ON dmgr.dept_no = dpt.dept_no
JOIN employees AS e
ON dmgr.emp_no = e.emp_no;


SELECT employees.emp_no, employees.last_name, employees.first_name, departments.dept_name
FROM employees
JOIN dept_emp
ON dept_emp.emp_no = employees.emp_no
JOIN departments 
ON dept_emp.dept_no = departments.dept_no;


SELECT first_name, last_name, sex
FROM employees
WHERE first_name = 'Hercules' 
AND last_name LIKE 'B%';


SELECT employees.emp_no, employees.last_name, employees.first_name, departments.dept_name
FROM employees
JOIN dept_emp
ON dept_emp.emp_no = employees.emp_no
JOIN departments 
ON dept_emp.dept_no = departments.dept_no
WHERE dept_name = 'Sales';


SELECT employees.emp_no, employees.last_name, employees.first_name, departments.dept_name
FROM employees
JOIN dept_emp
ON dept_emp.emp_no = employees.emp_no
JOIN departments 
ON dept_emp.dept_no = departments.dept_no
WHERE dept_name = 'Sales' OR dept_name = 'Development';


SELECT last_name, COUNT(last_name) AS "last_name_count"
FROM employees
GROUP BY last_name
ORDER BY "last_name_count" DESC;

