
# Student Grade Calculator

def calculate_grade(average):
    if average >= 75:
        return "A"
    elif average >= 65:
        return "B"
    elif average >= 55:
        return "C"
    elif average >= 35:
        return "S"
    else:
        return "F"


# Get student details
student_name = input("Enter student name: ")
num_subjects = int(input("Enter number of subjects: "))

marks = []

# Get subject marks
for i in range(num_subjects):
    mark = float(input(f"Enter marks for subject {i + 1}: "))

    if mark < 0 or mark > 100:
        print("Invalid marks! Enter a value between 0 and 100.")
        break

    marks.append(mark)

# Calculate results
if len(marks) == num_subjects and num_subjects > 0:

    total = sum(marks)
    average = total / num_subjects
    grade = calculate_grade(average)

    # Display results
    print("\n===== STUDENT REPORT =====")
    print("Student Name:", student_name)
    print("Total Marks:", total)
    print("Average:", round(average, 2))
    print("Final Grade:", grade)

    if grade == "F":
        print("Performance: Needs Improvement")
    else:
        print("Performance: Good Job!")

else:
    print("Unable to generate report. Check your inputs.")
