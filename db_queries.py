class DbQueries:
    CREATE_DATABASE_QUERY = "CREATE DATABASE IF NOT EXISTS challenge_db"
    CREATE_EMPLOYEES_TABLE_QUERY = "CREATE TABLE IF NOT EXISTS employees (" + \
                                   "id INT AUTO_INCREMENT PRIMARY KEY, " + \
                                   "employee_name VARCHAR(100)," + \
                                   "hire_date VARCHAR(100) UNIQUE NOT NULL," + \
                                   "job_id INT NOT NULL," + \
                                   "department_id INT NOT NULL," + \
                                   "FOREIGN KEY (job_id) REFERENCES jobs(id)," + \
                                   "FOREIGN KEY (department_id) REFERENCES departments(id)" + \
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
