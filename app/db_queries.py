class DbQueries:
    CREATE_DATABASE_QUERY = "CREATE DATABASE IF NOT EXISTS challenge_db"
    CREATE_EMPLOYEES_TABLE_QUERY = "CREATE TABLE IF NOT EXISTS employees (" + \
                                   "id INT AUTO_INCREMENT PRIMARY KEY, " + \
                                   "employee_name VARCHAR(200)," + \
                                   "hire_date DATETIME," + \
                                   "department_id INT NOT NULL," + \
                                   "job_id INT NOT NULL," + \
                                   "FOREIGN KEY (department_id) REFERENCES departments(id)" + \
                                   "FOREIGN KEY (job_id) REFERENCES jobs(id)," + \
                                   ")"
    CREATE_DEPARTMENTS_TABLE_QUERY = "CREATE TABLE IF NOT EXISTS departments " + \
                                     "(" + \
                                     "id INT AUTO_INCREMENT PRIMARY KEY, " + \
                                     "department VARCHAR(200) " + \
                                     ")"
    CREATE_JOBS_TABLE_QUERY = "CREATE TABLE IF NOT EXISTS jobs " + \
                              "(" + \
                              "id INT AUTO_INCREMENT PRIMARY KEY, " + \
                              "job VARCHAR(200) " + \
                              ")"
