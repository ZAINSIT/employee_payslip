from flask import Flask, render_template, request, redirect, url_for
from database import init_db
from models import (
    add_employee,
    get_all_employees,
    get_employee_by_id,
    save_payslip,
    get_latest_payslip
)
from salary_utils import calculate_salary

app = Flask(__name__)

init_db()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/employees")
def employees():
    employee_list = get_all_employees()
    return render_template("employees.html", employees=employee_list)

@app.route("/add_employee", methods=["GET", "POST"])
def add_employee_page():
    if request.method == "POST":
        emp_name = request.form["emp_name"]
        department = request.form["department"]
        designation = request.form["designation"]
        basic_salary = float(request.form["basic_salary"])
        hra = float(request.form["hra"])
        da = float(request.form["da"])
        bonus = float(request.form["bonus"])
        pf = float(request.form["pf"])
        tax = float(request.form["tax"])
        other_deductions = float(request.form["other_deductions"])

        add_employee(
            emp_name, department, designation, basic_salary,
            hra, da, bonus, pf, tax, other_deductions
        )
        return redirect(url_for("employees"))

    return render_template("add_employee.html")

@app.route("/generate_payslip", methods=["GET", "POST"])
def generate_payslip():
    employee_list = get_all_employees()
    if request.method == "POST":
        emp_id = int(request.form["emp_id"])
        pay_month = request.form["pay_month"]
        total_days = int(request.form["total_days"])
        leave_days = int(request.form["leave_days"])

        employee = get_employee_by_id(emp_id)
        if not employee:
            return "Employee not found"

        salary_data = calculate_salary(employee, total_days, leave_days)

        save_payslip(
            emp_id,
            pay_month,
            total_days,
            leave_days,
            salary_data["lop_days"],
            salary_data["per_day_salary"],
            salary_data["leave_deduction"],
            salary_data["gross_salary"],
            salary_data["total_deductions"],
            salary_data["net_salary"]
        )
        return redirect(url_for("view_payslip", emp_id=emp_id))

    return render_template("generate_payslip.html", employees=employee_list)

@app.route("/payslip/<int:emp_id>")
def view_payslip(emp_id):
    employee = get_employee_by_id(emp_id)
    payslip = get_latest_payslip(emp_id)

    if not employee or not payslip:
        return "Payslip not found"

    return render_template("payslip.html", employee=employee, payslip=payslip)

if __name__ == "__main__":
    app.run(debug=True)