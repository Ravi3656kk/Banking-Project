def get_student_info():
    name = input("Enter a candidate name: ")
    roll_no = input("Enter a candidate roll no: ")
    class_name = input("Enter class: ")
    return {
        "name": name,
        "class": class_name,
        "roll_no": roll_no
    }

# function to get subject marks
def get_marks(subjects):
    marks = []
    for subject in subjects:
        while True:
            try:
                score = int(input(f"Enter marks for {subject}: "))
                if 0 <= score <= 100:
                    marks.append(score)
                    break
                else:
                    print("Invalid input. Please enter a valid number between 0 and 100.")
            except:
                print("Invalid input. Please enter a number.")
    return marks

#function to calculate 
def calculate_total_and_avrage(marks):
    total = sum(marks)
    avrege = total / len(marks)
    return total/len(avrege)

def assign_grade(Averagr):
    if Averagr >=90:
      return "a"
    elif Averagr >= 75:
        return "b"
    elif Averagr >=50:
        return "c"
    else:
        return "fail"

#functio to print student report
def print_report(info,marks,total,Average,grade):
    print("\n..Student report..")
    print(f"...........................")
    print(f"name      : {info['name']}")
    print(f"class     : {info['class']}")
    print(f"roll_no      : {info['roll_no']}")
    print("marks      :", marks)
    print(f"total     :{total}")
    print(f"Average   :{Average:2f}")
    print(f"grade     :{grade}")
    print(".................\n")
    

#using recursion(recurcive function)
def run_program():
    subijects = ["math","socal scince", "scince","math"]
    student_info = get_student_info()
    marks = get_marks(subijects)
    total, average = calculate_total_and_avrage(marks)
    grade = assign_grade(average)
    print_report(student_info, marks, total, grade)

choice = input("do you want to enter another candodate details?  (yes/no): ")
if choice.lower() == "yes":
    run_program()
else:
    print("program ended. thanku gandu aise hi check karte raho")
run_program()

