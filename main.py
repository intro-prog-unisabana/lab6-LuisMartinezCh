from grades_manager import *


def main():

    print("Welcome to the Student Grades Manager!\n")

    my_grades = {}

    while True:

        print("Select an option:")
        print("1. Add a student")
        print("2. Print student grade averages")
        print("3. Exit")

        choice = input().strip()

        if choice == "1":
            my_grades = add_student(my_grades)

        elif choice == "2":

            print("Select an option:")
            print("a. Display all students")
            print("b. Display selected students")

            option = input().strip().lower()

            if option == "a":
                avg_by_student(my_grades)

            elif option == "b":
                print("Enter student names (comma-separated):")
                names = input().split(",")

                names = [n.strip() for n in names]

                avg_by_student(my_grades, names)

            else:
                print("Invalid option selected!")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option selected!")


if __name__ == "__main__":
    main()