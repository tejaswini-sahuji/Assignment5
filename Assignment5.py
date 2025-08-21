#Create dictionary of student marks
#Task 1
student_marks = {
    "Alice": 85,
    "Bob": 78,
    "Charlie": 92,
    "Diana": 88,
    "Ethan": 74
}
#take user input
student_name = input("Enter student name : ")
#condition if student name is matched with key of student_marks variable
if student_name in student_marks:
    print(f"{student_name} marks : {student_marks[student_name]}")
else:
    print("Student not found")

#task2

# Step 1: Create a list of numbers from 1 to 10
number = list(range(1,11))
# Step 2: Extract the first five elements
first_five =(number[:5])
# Step 3: Reverse the extracted elements
reversed_five = first_five[::-1]
# Step 4: Print both the extracted list and the reversed list
print("First five elements :", first_five)

print("Reversed five elements :", reversed_five)
