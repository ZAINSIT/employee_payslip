# Employee Payslip Generator

A Python-based Employee Payslip Generator that creates employee salary slips from salary and payroll details. The application calculates earnings and deductions, generates a formatted payslip, and supports printing the final document.

## Features

- Add employee information.
- Enter salary and payroll details.
- Calculate allowances and deductions.
- Calculate gross salary and net salary.
- Generate a formatted employee payslip.
- Print the generated payslip.
- Store or display employee payroll information.
- Simple and user-friendly interface.
- Reduces manual payroll calculation errors.

## Technologies Used

- Python
- SQL or SQLite
- Flask

## Salary Calculation

The application can calculate salary using the following structure:

```text
Gross Salary = Basic Salary + Allowances

Total Deductions = Tax + Insurance + Other Deductions

Net Salary = Gross Salary - Total Deductions
```

The exact calculation depends on the salary details entered by the user.

## Payslip Details

A generated payslip may contain:

- Company name and address.
- Employee name.
- Employee ID.
- Department.
- Designation.
- Pay period.
- Basic salary.
- House rent allowance.
- Transport allowance.
- Other allowances.
- Tax deductions.
- Insurance deductions.
- Other deductions.
- Gross salary.
- Net salary.
- Date of generation.
- Employee and authorized signatures.

## Printing Support

After generating the payslip, the application provides a print option. The payslip can be formatted for printing on standard paper. Depending on the implementation, printing may be handled using:

- A generated PDF file.
- The system print dialog.
- Browser-based printing.
- A GUI print command.

## Installation

Clone the repository:

```bash
git clone https://github.com/ZAINSIT/employee_payslip.git
```

Move into the project directory:

```bash
cd employee_payslip
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Activate it on macOS or Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

If the project does not have a `requirements.txt` file, install the packages used by your application manually.

## Running the Application

Run the main Python file:

```bash
python main.py
```

If your entry file has a different name, replace `main.py` with the correct filename.

## Usage

1. Start the application.
2. Enter the employee details.
3. Enter the salary and deduction information.
4. Select the calculation or generate option.
5. Review the gross salary, deductions, and net salary.
6. Generate the payslip.
7. Select the print option to print the payslip.
8. Save a copy if the application supports file export.

## Project Structure

```text
employee_payslip/
│
├── main.py
├── database.py
├── salary_calculator.py
├── payslip_generator.py
├── print_service.py
├── templates/
├── static/
├── requirements.txt
└── README.md
```

The exact structure may differ depending on your implementation.

## Example Calculation

```text
Basic Salary:       ₹30,000
Allowances:         ₹5,000
Gross Salary:       ₹35,000

Deductions:         ₹3,000

Net Salary:         ₹32,000
```

## Future Improvements

- User login and role-based access.
- Employee database management.
- Monthly payroll history.
- PDF download and email support.
- Automatic tax calculation.
- Multiple payslip templates.
- Bulk payslip generation.
- Export to Excel.
- Cloud deployment.
- Improved validation and reporting.

## Disclaimer

This project is intended for educational and demonstration purposes. Salary, tax, and deduction calculations should be configured according to the organization’s payroll policies and applicable regulations.
