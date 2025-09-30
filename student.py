class Student:
    def __init__(self, name, roll_number, grade, major):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade
        self.major = major

    def display_details(self):
        print("\n--- Student Details ---")
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Grade: {self.grade}")
        print(f"Major: {self.major}")

def get_student_input():
    name = input("Enter student's name: ")
    roll_number = input("Enter student's roll number: ")
    grade = input("Enter student's grade: ")
    major = input("Enter student's major: ")
    return Student(name, roll_number, grade, major)

if __name__ == "__main__":
    student1 = get_student_input()
    student1.display_details()

    # You can create more student objects as needed
    # student2 = get_student_input()
    # student2.display_details()