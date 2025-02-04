courses = {
    "MAT-035": {"desc": "Concepts of Algebra", "tuition": 460},
    "CTI-115": {"desc": "Computer System Foundations", "tuition": 520.98},
    "BAS-120": {"desc": "Intro to Analytics", "tuition": 500},
    "CSC-121": {"desc": "Python Programming", "tuition": 783.88}
}

students = {
    "Zakari Watson": ["CTI-115", "CSC-121"],
    "Jerom Williams": ["CTI-115", "CSC-121", "MAT-035", "BAS-120"],
    "Dominique Ross": ["CTI-115", "CSC-121", "MAT-035"],
    "Diana Shepard": ["MAT-035", "CTI-115", "BAS-120", "CSC-121"],
    "Yoko Mayo": ["MAT-035"],
    "Rashad Ahmed": ["MAT-035", "BAS-120"],
    "Susan Jones": ["BAS-120", "CSC-121"]
}

def display_courses():
    '''
    displays courses and tuition
    Returns: none
    '''
    course = "Course Name"
    cost = "Tuition"
    print(f"{course:<50} {cost}")
    print("- " * 33)
    for key in courses.keys():
        print(f"{courses[key]["desc"]:<50} ${courses[key]["tuition"]}")
    print("- " * 33)

def lookup():
    '''
    displays the info of a specific course
    Return: none
    '''
    code = input("Enter the course code: ")
    print()
    if code in courses:
        course = "Course Name"
        cost = "Tuition"
        print(f"{course:<50} {cost}")
        print(f"{courses[code]["desc"]:<50} ${courses[code]["tuition"]}")
    else:
        print(f"Course {code} is not being offered.")

def display_students():
    # create a list of student names to loop thru
    names_list = list(students.keys())
    count = 1
    for i in names_list:
        print(f"{count}) {i}")
        count += 1
    choice = int(input("Choose a student: "))
    # validate choice
    if choice < 1 or choice > 7:
        choice = int(input("Invalid entry. Try again: "))
    # create a list of classes to loop thru
    person = names_list[choice - 1]
    class_list = students[person]
    print()
    print(f"{person}'s Courses and Tuition: ")
    print("- " * 33)
    # create a list to store total tuition
    tuition_list = []
    for i in range(len(class_list)):
        code = students[person][i]
        print(f"{code:<10}{courses[code]["desc"]:<40}${courses[code]["tuition"]}")
        tuition_list.append(courses[code]["tuition"])
    print("- " * 33)
    total = "Overall Total"
    print(f"{total:<51}${sum(tuition_list):.2f}")

def total_tuition():
    name = "Student Name"
    num = "# of Courses"
    cost = "Tuition"
    print(f"{name:<20}{num:<20}{cost}")
    print("- " * 33)
    mega_tuition = 0
    for s in students:
        total_tuition = 0
        num_classes = 0
        # loop thru each students classes
        for c in students[s]: 
            for course in courses: 
                if c == course:
                    num_classes += 1
                    student_tuition = courses[course]["tuition"]
                    total_tuition += student_tuition
        mega_tuition += total_tuition
        print(f"{s:<20}{(num_classes):<20}${total_tuition:.2f}")
    text = "Overall Total:"
    print(f"{text:<40}${mega_tuition:.2f}")
    print("- " * 33)
        
        


    

    
    
    
    

   