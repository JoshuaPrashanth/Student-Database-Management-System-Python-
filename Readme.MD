# 🧑‍🎓 Student Database Management System (Python)

A simple **Student Database Management System** written in **Python**, using the **Pandas** library to organize and export student data to CUSTOM PATH.  
This program runs entirely in the **terminal** and allows users to manage student records interactively.

---

## 📋 Features

- ➕ Add new students to the database  
- ➖ Remove students from the database  
- 👀 View list of all students  
- 📄 View individual student details  
- 🧮 Calculate and display grades based on marks  
- 📊 Show all student details in tabular form  
- 📂 Export student records to an Excel spreadsheet to CUSTOM PATH  
- 🧹 Clear the entire database  
- 🚪 Exit safely

---

## 🧠 How It Works

The system uses a `Student` class to store individual student details (name, roll number, and marks).  
All students are kept in Python lists (`student_list` and `student_name_list`) while the program runs.  
A helper function `get_data()` converts this in-memory data into a **Pandas DataFrame** for display and exporting.

---

## 🏗️ Code Overview

### 🧾 Class: `Student`
```python
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
