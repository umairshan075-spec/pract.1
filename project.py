import os

FILENAME = "students.txt"

# Function to add student
def add_student():
    with open(FILENAME, "a") as file:
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")
        file.write(roll + "," + name + "," + marks + "\n")
    print("Student added successfully!\n")


# Function to display all students
def display_students():
    if not os.path.exists(FILENAME):
        print("No records found.\n")
        return
    
    with open(FILENAME, "r") as file:
        print("\n--- Student Records ---")
        for line in file:
            roll, name, marks = line.strip().split(",")
            print(f"Roll: {roll}, Name: {name}, Marks: {marks}")
    print()


# Function to search student
def search_student():
    roll_search = input("Enter Roll Number to search: ")
    found = False

    if not os.path.exists(FILENAME):
        print("No records found.\n")
        return

    with open(FILENAME, "r") as file:
        for line in file:
            roll, name, marks = line.strip().split(",")
            if roll == roll_search:
                print(f"Found -> Roll: {roll}, Name: {name}, Marks: {marks}\n")
                found = True
                break

    if not found:
        print("Student not found.\n")


# Function to delete student
def delete_student():
    roll_delete = input("Enter Roll Number to delete: ")
    lines = []
    found = False

    if not os.path.exists(FILENAME):
        print("No records found.\n")
        return

    with open(FILENAME, "r") as file:
        lines = file.readlines()

    with open(FILENAME, "w") as file:
        for line in lines:
            roll, name, marks = line.strip().split(",")
            if roll != roll_delete:
                file.write(line)
            else:
                found = True

    if found:
        print("Student deleted successfully!\n")
    else:
        print("Student not found.\n")


# Main Menu
while True:
    print("===== Umair's Student Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.\n")
