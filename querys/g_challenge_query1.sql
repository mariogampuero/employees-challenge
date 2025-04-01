SELECT 
    d.department_name AS department, 
    j.job_title AS job, 
    SUM(CASE WHEN MONTH(e.hire_date) BETWEEN 1 AND 3 THEN 1 ELSE 0 END) AS Q1,
    SUM(CASE WHEN MONTH(e.hire_date) BETWEEN 4 AND 6 THEN 1 ELSE 0 END) AS Q2,
    SUM(CASE WHEN MONTH(e.hire_date) BETWEEN 7 AND 9 THEN 1 ELSE 0 END) AS Q3,
    SUM(CASE WHEN MONTH(e.hire_date) BETWEEN 10 AND 12 THEN 1 ELSE 0 END) AS Q4
FROM hr.employees e 
LEFT JOIN hr.departments d ON e.department_id = d.department_id
LEFT JOIN hr.jobs j ON e.job_id = j.job_id
WHERE YEAR(e.hire_date) = 1997
GROUP BY d.department_name, j.job_title
ORDER BY d.department_name ASC, j.job_title ASC;