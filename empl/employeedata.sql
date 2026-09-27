CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY,
    employee_name TEXT NOT NULL,
    designation TEXT,
    joining_date TEXT,
    basic_salary REAL NOT NULL,
    bank_account TEXT
);

CREATE TABLE salary_components (
    component_id INTEGER PRIMARY KEY,
    emp_id INTEGER,
    hra REAL DEFAULT 0,
    da REAL DEFAULT 0,
    bonus REAL DEFAULT 0,
    pf REAL DEFAULT 0,
    tax REAL DEFAULT 0,
    other_deductions REAL DEFAULT 0,
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
);

CREATE TABLE payslips (
    payslip_id INTEGER PRIMARY KEY,
    emp_id INTEGER,
    pay_month TEXT,
    gross_salary REAL,
    total_deductions REAL,
    net_salary REAL,
    generated_on TEXT,
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
);