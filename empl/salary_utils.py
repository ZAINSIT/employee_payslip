def calculate_salary(employee, total_days, leave_days, allowed_leaves=2):
    basic_salary = employee["basic_salary"]
    hra = employee["hra"]
    da = employee["da"]
    bonus = employee["bonus"]
    pf = employee["pf"]
    tax = employee["tax"]
    other_deductions = employee["other_deductions"]

    gross_salary = basic_salary + hra + da + bonus
    total_deductions = pf + tax + other_deductions

    # Leave / LOP calculation
    per_day_salary = gross_salary / total_days if total_days > 0 else 0
    lop_days = max(0, leave_days - allowed_leaves)
    leave_deduction = round(per_day_salary * lop_days, 2)

    net_salary = gross_salary - total_deductions - leave_deduction

    return {
        "gross_salary": gross_salary,
        "total_deductions": total_deductions,
        "per_day_salary": round(per_day_salary, 2),
        "lop_days": lop_days,
        "leave_deduction": leave_deduction,
        "net_salary": round(net_salary, 2)
    }