# Write your code here!
def employee_print(employee_info):
    for key, value in employee_info.items():
        if value is None:
            print(f"{key}: N/A")
        else:
            print(f"{key}: {value}")

    if len(employee_info) < 3:
        print("No other info!")
    if len(employee_info) == 0:
        print("Name: N/A")
