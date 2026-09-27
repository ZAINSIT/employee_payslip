from database import get_connection

def add_employee(emp_name, department, designation, basic_salary,
                 hra, da, bonus, pf, tax, other_deductions):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO employees
        (emp_name, department, designation, basic_salary, hra, da, bonus, pf, tax, other_deductions)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (emp_name, department, designation, basic_salary, hra, da, bonus, pf, tax, other_deductions))
    conn.commit()
    conn.close()

def get_all_employees():
    conn = get_connection()
    employees = conn.execute("SELECT * FROM employees").fetchall()
    conn.close()
    return employees

def get_employee_by_id(emp_id):
    conn = get_connection()
    employee = conn.execute("SELECT * FROM employees WHERE emp_id = ?", (emp_id,)).fetchone()
    conn.close()
    return employee

def save_payslip(emp_id, pay_month, total_days, leave_days, lop_days,
                  per_day_salary, leave_deduction, gross_salary,
                  total_deductions, net_salary):
    conn = get_connection()
    conn.execute("""
        INSERT INTO payslips
        (emp_id, pay_month, total_days, leave_days, lop_days, per_day_salary,
         leave_deduction, gross_salary, total_deductions, net_salary)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (emp_id, pay_month, total_days, leave_days, lop_days, per_day_salary,
          leave_deduction, gross_salary, total_deductions, net_salary))
    conn.commit()
    conn.close()

# get_latest_payslip stays the same — it just selects * so new columns come along automatically

def get_latest_payslip(emp_id):
    conn = get_connection()
    payslip = conn.execute("""
        SELECT * FROM payslips
        WHERE emp_id = ?
        ORDER BY payslip_id DESC
        LIMIT 1
    """, (emp_id,)).fetchone()
    conn.close()
    return payslip