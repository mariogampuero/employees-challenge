class DbQueries:
    create_database_query = "CREATE DATABASE IF NOT EXISTS challenge_db"
    create_employees_table_query = "CREATE TABLE IF NOT EXISTS employees (" + \
                                   "id INT AUTO_INCREMENT PRIMARY KEY, " + \
                                   "employee_name VARCHAR(100)," + \
                                   "hire_date VARCHAR(100) UNIQUE NOT NULL," + \
                                   "job_id INT NOT NULL," + \
                                   "department_id INT NOT NULL," + \
                                   "FOREIGN KEY (job_id) REFERENCES jobs(id)," + \
                                   "FOREIGN KEY (department_id) REFERENCES departments(id)" + \
                                   ")"
    create_departments_table_query = "CREATE TABLE IF NOT EXISTS departments " + \
                                     "(" + \
                                     "id INT AUTO_INCREMENT PRIMARY KEY, " + \
                                     "department VARCHAR(200) " + \
                                     ")"
    create_jobs_table_query = "CREATE TABLE IF NOT EXISTS jobs " + \
                              "(" + \
                              "id INT AUTO_INCREMENT PRIMARY KEY, " + \
                              "job VARCHAR(200) " + \
                              ")"
