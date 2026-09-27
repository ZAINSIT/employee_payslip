import sqlite3

DB_NAME = "payroll.db"

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
            emp_name TEXT NOT NULL,
            department TEXT,
            designation TEXT,
            basic_salary REAL NOT NULL,
            hra REAL DEFAULT 0,
            da REAL DEFAULT 0,
            bonus REAL DEFAULT 0,
            pf REAL DEFAULT 0,
            tax REAL DEFAULT 0,
            other_deductions REAL DEFAULT 0
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS payslips (
            payslip_id INTEGER PRIMARY KEY AUTOINCREMENT,
            emp_id INTEGER,
            pay_month TEXT,
            total_days INTEGER,
            leave_days INTEGER,
            lop_days INTEGER,
            per_day_salary REAL,
            leave_deduction REAL,
            gross_salary REAL,
            total_deductions REAL,
            net_salary REAL,
            generated_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
        )
    """)
    conn.commit()
    conn.close()