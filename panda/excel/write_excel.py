import openpyxl #pip install openpyxl

from openpyxl.workbook import Workbook

# Create a workbook and sheets
wb = Workbook()
sheet1 = wb.active
sheet1.title = "Sales Data"
sheet2 = wb.create_sheet(title="Employee Data")

# Sales Data
sales_data = [
    ["Date", "Product", "Region", "Sales", "Profit"],
    ["2023-01-01", "A", "North", 1000, 200],
    ["2023-01-01", "B", "South", 1500, 300],
    ["2023-01-02", "A", "East", 1200, 250],
    ["2023-01-02", "C", "West", 800, 150],
    ["2023-01-03", "B", "North", 1300, 220],
    ["2023-01-03", "C", "South", 1100, 180],
]

for row in sales_data:
    sheet1.append(row)

# Employee Data
employee_data = [
    ["Employee ID", "Name", "Department", "Salary"],
    [1, "John Doe", "Sales", 60000],
    [2, "Jane Smith", "Marketing", 65000],
    [3, "Jim Brown", "IT", 70000],
    [4, "Jake White", "HR", 55000],
]

for row in employee_data:
    sheet2.append(row)

# Save the workbook
wb.save("/Users/nomixe/Documents/python/panda/excel/data.xlsx")
