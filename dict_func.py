# Write your code here!
def employee_print(employee_info):
    
    if not employee_info:
        employee_info = {"Name": None, "Salary": None, "Role": None}
    
    for key, value in employee_info.items():
        if value is None:
            print(f"{key}: N/A")
        else:
            print(f"{key}: {value}")
    
    if len(employee_info) <= 3:
        print("No other info!")