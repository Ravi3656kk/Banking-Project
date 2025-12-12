name = input("Enter your name. ")
roll_no = int(input("Enter your roll no. "))
student_class = int(input("Enter your class. "))

subjects = ["math", "science", "english"]
marks = {}

for subject in subjects:
      score = int(input(f"enter marks for {subject}: "))
      marks[subject] = score

total = sum(marks.values())
average = total / len(subjects)

if average >= 90:
      grade = "A"
elif average >= 75:
      grade = "B"
elif average >= 50:
      grade = "C"

else:
      grade ="fail"

print("Name", name)
print("Roll_no", roll_no)
print("Class", student_class)
print("subiject-wise marks: ")
print("subject-wise marks: ")
for subject, mark in marks.items():
      print(f" {subject}: {mark}")

print("total marks:", total)
print("average marks:", round(average,2))
print("grade:", grade)