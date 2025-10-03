import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame


class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display(self):
        print(f"\n----Student details----\n"
              f"Name : {self.name}\n"
              f"Roll Number : {self.roll_number}\n"
              f"Marks : {self.marks}")

    def calculate_grade(self):
        if self.marks >= 90:
            print("Grade : A")
        elif self.marks >= 75:
            print("Grade : B")
        elif self.marks >= 50:
            print("Grade : C")
        else:
            print("Grade : F")

student_list = []
student_name_list = []
all_student = []
while True:
    print("\n---------------------------------------------------------------------------------------------------------------")
    print("STUDENT DATABASE")
    print("---------------------------------------------------------------------------------------------------------------")

    print("1. Add Student to DataBase")
    print("2. Remove Student from DataBase")
    print("3. View Database")
    print("4. View Student Details")
    print("5. View Grade of Student")
    print("6. Show all students Details")
    print("7. Get CSV Record")
    print("8. Clear DataBase")
    print("9. Exit")
    choice = input("Select for operation : ")
    print()
    if choice == "1":


        student_name = input("Enter student name: ")
        student_name = student_name.title()
        student_USN = input("Enter student USN (last 3 digit): ")
        student_USN = '4MH24CS' + student_USN
        student_marks = int(input("Enter student Marks (out of 100): "))

        student = Student(student_name, student_USN, student_marks)
        student_list.append(student)
        student_name_list.append(student.name)
        all_student = student_name_list.copy()
        student_name_list.sort()

        print()
        print(f"New student \"{student_name}\" ADDED to DataBase")



    elif choice == "2":


        name = input("Enter student name: ")
        name = name.title()
        for i in student_list:
            if i.name == name:
                student_list.remove(i)
                student_name_list.remove(i.name)
                print(f"Student \"{i.name}\" has been removed.")
                break
        else:
            print("Student not found in DataBase.")


    elif choice == "3":


        if not student_list:
            print("Database is Empty")
        else:
            for i,s in enumerate(student_name_list, start=1):
                print(str(i)+ ". " + s)

    elif choice == "4":

        name = input("Enter Student name: ")
        name = name.title()

        for i in student_list:
            if i.name == name:
                i.display()
                break
        else:
            print("Student not found in DataBase.")

    elif choice == "5":
            search_name = input("Enter Student name: ")
            search_name = search_name.title()

            for i in student_list:
                if i.name == search_name:
                    i.calculate_grade()
                    break
            else:
                print("Student not found in DataBase.")

    elif choice == "6":
        if not student_list:
            print("DataBase is Empty")
        else:
            marks_list = []
            Roll_number_list = []
            for i in student_list:
                marks_list.append(i.marks)
                Roll_number_list.append(i.roll_number)
            data = {"Name": all_student, "USN": Roll_number_list, "Marks": marks_list}
            df = pd.DataFrame(data)
            print(df)

    elif choice == "7":
        if not student_list:
            print("DataBase is Empty")
        else:
            df.to_csv(r"C:\Users\prash\OneDrive\Desktop\PythonProject\Student Database Management System\CSV_Record.csv")
            print("CSV has been Downloaded.")

    elif choice == "8":
        confirm = input("Are you sure to CLEAR the database? (y/n) : ")
        if confirm == "y":
            student_list = []
            student_name_list = []
            print("DataBase has been CLEARED.")
        elif confirm != "n":
            print("Invalid Input!")

    elif choice == "9":

        print("Thank You!!")
        break

    else:
        print("Invalid Input!")


