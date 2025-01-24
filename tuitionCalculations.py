# define lists
stu_names = ["Zakari Watson", "Jerom Williams", "Dominique Ross", "Diana Shepard", "Yoko Mayo", "Rashad Ahmed", "Susan Jones"]
courses = ["MAT 035(Concepts of Algebra)", "CTI 115(Computer Systems Foundation)", "BAS 120 Intro to Analytics", "CSC 121 Python Progamming"]
tuition = [460, 520.98, 500, 783.88]

def calc_full_tuition():
    '''
    determines what classes each student will take and add the cost
    Return: none
    '''
    # create a list to store costs(hardcoding 0 ensures all student's tuition will be displayed even if it's 0)
    tuition_per_student = [0,0,0,0,0,0,0]
    # loop thru list of names and costs
    for i in range(7):
        cost = 0
        for x in range (4):
            print("Enter 'y' for yes: ")
            answer = input(f"Is {stu_names[i]} taking {courses[x]}? ")
            # if the student is taking the class, add the cost to the list
            if answer.lower() == "y": 
                cost += (tuition[x])
                tuition_per_student[i] = cost
    stu = "Student Name"
    tui = "Tuition"
    print()
    # display costs
    print(f"{stu:<24}{tui}")
    print("- " * 16)
    for i in range(7):
        print(f"{stu_names[i]:<24}${tuition_per_student[i]:.2f}")
    print("- " * 16)


def calc_single_tuition(num):
    '''
    Determines which classes a specific student will take and adds the cost
    Return: none
    '''
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
    
def choose_student():
    '''
    Lets the user choose a specific student
    Return: user's choice
    '''
    print("\n\nSelect from the list of student names below: ")
    for i in range(7):
        print(f"{i+1}) {stu_names[i]} ")
    print()
    choice = int(input("Enter student number: "))
    if choice < 1 or choice > 7:
        choice = int(input("Invalid entry. Please try again: "))
    return choice