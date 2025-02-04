
import menu_functions as im

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

# Just an example to remind you how to pull data from a nested dictionary

def main():
    choice = menu()
    evaluate_choice(choice)

def menu():
    print("- " * 12, "MENU ", "- " * 12)
    print("1) Display Course Information")
    print("2) Lookup Course")
    print("3) Display Courses and Tuition for Specific Student")
    print("4) Display Tuition for All Students")
    print("5) Display Number of Students and Tuition for All Courses")
    print("6) Exit")
    print("- " * 12, "MENU ", "- " * 12)
    choice = int(input("Select an option: "))
    return choice

def evaluate_choice(x):
    while x != 6:
        if x == 1:
            print()
            im.display_courses()
            print()
            choice = menu()
            evaluate_choice(choice)
        elif x == 2:
            print()
            im.lookup()
            print()
            choice = menu()
            evaluate_choice(choice)
        elif x == 3:
            print()
            im.display_students()
            print()
            choice = menu()
            evaluate_choice(choice)
        elif x == 4:
            print()
            im.total_tuition()
            print()
            choice = menu()
            evaluate_choice(choice)
        elif x == 5:
            print()
            print()
            choice = menu()
            evaluate_choice(choice)
        elif x < 1 or x > 6:
            print()
        
            x = int(input("Invalid entry. Please try again: "))
    print("Program exiting...") # need to fix, it keeps showing the menu again after printing

# Call the main
if __name__ == "__main__":
    main()