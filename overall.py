def student_averages(students):
    averages = {}
    for student, data in students.items():
        average_std = sum(data.values()) / len(data)
        averages[student] = round(average_std)
    return averages

def assignment_averages(students):
    if not students:
        return {}
    averages = {}
    for homework in next(iter(students.values())).keys():
        total = 0
        for student, data in students.items():
            total += data[homework]
        averages[homework] = round(total / len(students))
    return averages
