def student_averages(students):
    averages = {}
    for student, data in students.items():
        average_std = sum(data.values()) / len(data)
        averages[student] = round(average_std)
    print(averages)

def assignment_averages(students):
    averages = {}
    for homework in students["s1"].keys():
        total = 0
        for student, data in students.items():
            total += data[homework]
        average_hw = total / len(students)
        averages[homework] = round(average_hw)
    print(averages)