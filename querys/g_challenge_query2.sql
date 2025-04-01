WITH conteo_departamentos AS (
    SELECT d.department_id, d.department_name, COUNT(e.employee_id) AS conteo_empleados
    FROM employees e 
    LEFT JOIN departments d ON e.department_id = d.department_id
    WHERE YEAR(e.hire_date) = 1997
    GROUP BY d.department_id, d.department_name
)
SELECT department_id, department_name, conteo_empleados
FROM conteo_departamentos
WHERE conteo_empleados > (SELECT AVG(conteo_empleados) FROM conteo_departamentos);