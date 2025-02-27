import csv

stu_names = ["Zakari Watson", "Jerom Williams", "Dominique Ross", "Diana Shepard", "Yoko Mayo", "Rashad Ahmed", "Susan Jones"]
courses = ["MAT 035(Concepts of Algebra)", "CTI 115(Computer Systems Foundation)", "BAS 120 Intro to Analytics", "CSC 121 Python Progamming"]
tuition = [460, 520.98, 500, 783.88]


def read_csv(): # gpt helped
    students = {}
    
    with open("stu_courses.csv", newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
    
    # Check that we have at least one row (the header)
    if not rows:
        return students

    # The first row contains course names.
    course_names = [course.strip() for course in rows[0]]
    
    # Iterate over the rest of the rows.
    for row in rows[1:]:
        # Ensure the row has as many cells as there are courses (if not, pad with empty strings)
        if len(row) < len(course_names):
            row += [""] * (len(course_names) - len(row))
        for i, cell in enumerate(row):
            student_name = cell.strip()
            if student_name != "":
                course = course_names[i]
                # Initialize the student's dictionary if not already present.
                if student_name not in students:
                    students[student_name] = {}
                # Add the course to the student's record (if not already added).
                students[student_name][course] = None
    print(students)
    return students


def display_info():
    '''
    displays courses and tuition
    '''
    course = "Course Name"
    cost = "Tuition"
    print(f"{course:<50} {cost}")
    print("- " * 33)
    for i in range(4):
        print(f"{courses[i]:<50} ${tuition[i]}")
    print("- " * 33)

def menu():
    # display menu
    print("-" * 24, "MENU", "-" * 24)
    print("1) Select Courses, Course Grade, and Calculate Tuition")
    print("2) Calculate Tuition For Specific Students")
    print("3) Display Average and Total Tuition for All Students")
    print("4) Display Student Information")
    print("5) Exit")
    print("-" * 24, "MENU", "-" * 24)
    # get user's choice
    choice = int(input("Select an option: "))
    return choice

def evaluate_choice(choice,x):
    # call appropriate function given the user's choice
    while choice != 5: 
        if choice == 1:
            print()
            get_grade(x)
            print()
        elif choice == 2:
            print()
            calc_single_tuition()
            print()
        elif choice == 3:
            print()
            courses_info()
            print()
        elif choice == 4:
            print()
            stu_info()
            print()
        else:
            while choice < 1 or choice > 5:
                choice = int(input("Invalid entry. Try again: "))
        choice = menu() 
    print("Program exiting...")
    
def get_grade(x): # gpt helped, specifically for writing the file and getting the values out of the nested dictionary
    '''
    determines what classes each student will take and add the cost
    Return: none
    '''
    students = x
    # create a list to store costs(hardcoding 0 ensures all student's tuition will be displayed even if it's 0)
    tuition_per_student = [0,0,0,0,0,0,0]
    # loop thru list of names and costs
    for i in range(7):
        cost = 0
        grades = []
        for x in range (4):
            print("Enter 'y' for yes: ")
            answer = input(f"Is {stu_names[i]} taking {courses[x]}? ")
            # if the student is taking the class, add the cost to the list
            if answer.lower() == "y": 
                cost += (tuition[x])
                tuition_per_student[i] = cost
                # add student name to dict as a key
                if stu_names[i] not in students: 
                    students[stu_names[i]] = {}
                # get grade and add to the dict
                grade = float(input(f"Enter {stu_names[i]}'s grade for {courses[x]}: "))
                students[stu_names[i]][courses[x]] = grade
                grades.append(grade)
                # add average grade and tuition to the nested dictionary
                students[stu_names[i]]['avg'] = sum(grades)/len(grades)
                students[stu_names[i]]['tuition'] = cost
    with open("stu_courses.txt", "w") as file: 
        header = f"{'Student Name':<20}{'Average Grade':<20}{'Tuition':<10}\n"
        file.write(header)
        file.write("-" * 50 + "\n")
        # access the nested dictionary to write info
        for student in stu_names:
            avg = students.get(student, {}).get('avg', 0)
            tuit = students.get(student, {}).get('tuition', 0)
            line = f"{student:<20}{avg:<20.2f}${tuit:<10.2f}\n"
            file.write(line)


def calc_single_tuition():
    '''
    Determines which classes a specific student will take and adds the cost
    Return: none
    '''
    print("\n\nSelect from the list of student names below: ")
    for i in range(7):
        print(f"{i+1}) {stu_names[i]} ")
    print()
    num = int(input("Enter student number: "))
    if num < 1 or num > 7:
        num = int(input("Invalid entry. Please try again: "))
    cost = 0
    # create a list to store costs
    stu_tuition = []
    # create a new list to store only courses this specific student is taking
    new_courses = []
    # loop thru courses
    for x in range (4):
        cost = 0
        print("Enter 'y' for yes: ")
        answer = input(f"Is {stu_names[num-1]} taking {courses[x]}? ")
        # if the student is taking the course, and it and its cost to their respective lists
        if answer.lower() == "y": 
            cost += (tuition[x])
            stu_tuition.append(cost)
            new_courses.append(courses[x])
    course = "Course"
    tui = "Tuition"
    full_cost  = "Total Cost"
    print()
    # display courses and costs
    print(f"{course:<50}{tui}")
    print("- " * 33)
    for i in range (len(stu_tuition)):
        print(f"{new_courses[i]:<50}${stu_tuition[i]:.2f}")
    print("- " * 33)
    print(f"{full_cost:<50}${sum(stu_tuition):.2f}")
    print()
    # write info into a text file
    with open("student.txt", "w") as file:
        file.write(f"Student: {stu_names[num-1]}\n")
        file.write(f"{course:<50}{tui}\n")
        file.write("- " * 33 + "\n")
        for i in range (len(stu_tuition)):
            file.write(f"{new_courses[i]:<50}${stu_tuition[i]:.2f}\n")
        file.write("- " * 33 + "\n")
        file.write(f"{full_cost:<50}${sum(stu_tuition):.2f}")

def courses_info():
    # read file
    try:
        with open("stu_courses.txt", "r") as file:
            for line in file:
                line = line.rstrip('\n')
                print(line)
    except:
        print("File not found")

def stu_info():
    # read file
    try: 
        with open("student.txt", "r") as file:
            for line in file:
                line = line.rstrip('\n')
                print(line)
    except:
        print("File not found")