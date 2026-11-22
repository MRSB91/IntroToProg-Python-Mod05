# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Mahmoud Bza,11/22/2026,Implemented JSON storage, dictionaries, and error handling
# ------------------------------------------------------------------------------------------ #

# Import the json module
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:
    1. Register a Student for a Course.
    2. Show current data.
    3. Save data to a file.
    4. Exit the program.
-----------------------------------------
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
student_first_name: str = ""
student_last_name: str = ""
course_name: str = ""
student_data: dict = {}
students: list = []
file = None
menu_choice: str = ""

# Load existing enrollments when the program starts
try:
    file = open(FILE_NAME, "r", encoding="utf-8")
    loaded_data = json.load(file)
    if isinstance(loaded_data, list):
        students = loaded_data
    else:
        print("The JSON file must contain a list of student records.")
except FileNotFoundError:
    print("No saved enrollment file was found. Starting with an empty list.")
except (json.JSONDecodeError, UnicodeError) as error:
    print(f"Unable to read enrollment data: {error}")
except OSError as error:
    print(f"Unable to open enrollment file: {error}")
finally:
    if file is not None and not file.closed:
        file.close()

# Present and process the data
while menu_choice != "4":
    print(MENU)
    menu_choice = input("What would you like to do: ")

    if menu_choice == "1":
        # Ask for each required value; handle invalid or interrupted input
        try:
            student_first_name = input("Enter the student's first name: ").strip()
            if not student_first_name:
                raise ValueError("First name cannot be empty.")
        except (ValueError, EOFError, KeyboardInterrupt) as error:
            print(f"Unable to register student: {error}")
            continue

        try:
            student_last_name = input("Enter the student's last name: ").strip()
            if not student_last_name:
                raise ValueError("Last name cannot be empty.")
        except (ValueError, EOFError, KeyboardInterrupt) as error:
            print(f"Unable to register student: {error}")
            continue

        try:
            course_name = input("Please enter the name of the course: ").strip()
            if not course_name:
                raise ValueError("Course name cannot be empty.")
        except (ValueError, EOFError, KeyboardInterrupt) as error:
            print(f"Unable to register student: {error}")
            continue

        student_data = {
            "FirstName": student_first_name,
            "LastName": student_last_name,
            "CourseName": course_name
        }
        students.append(student_data)
        print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")

    elif menu_choice == "2":
        print("-" * 50)
        if not students:
            print("No student registrations found.")
        for student in students:
            print(f"{student['FirstName']},{student['LastName']},{student['CourseName']}")
        print("-" * 50)

    elif menu_choice == "3":
        # Write the list of dictionaries to JSON and close the file
        file = None
        try:
            file = open(FILE_NAME, "w", encoding="utf-8")
            json.dump(students, file, indent=4)
            print("The following data was saved to file!")
            for student in students:
                print(f"{student['FirstName']},{student['LastName']},{student['CourseName']}")
        except (OSError, TypeError, ValueError) as error:
            print(f"Could not save enrollment data: {error}")
        finally:
            if file is not None and not file.closed:
                file.close()

    elif menu_choice == "4":
        break
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")
