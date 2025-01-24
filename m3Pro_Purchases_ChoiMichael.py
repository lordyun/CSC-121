# Michael Choi
# 1-23-25
# CSC-121 m3Pro-Purchase
# This pogram allows the user to calculate tuition cost for students depending on the courses they are taking

# Import module
import tuitionCalculations as tc

# define lists
stu_names = ["Zakari Watson", "Jerom Williams", "Dominique Ross", "Diana Shepard", "Yoko Mayo", "Rashad Ahmed", "Susan Jones"]
courses = ["MAT 035(Concepts of Algebra)", "CTI 115(Computer Systems Foundation)", "BAS 120 Intro to Analytics", "CSC 121 Python Progamming"]
tuition = [460, 520.98, 500, 783.88]

def main():
    display_info()
    choice = menu()
    evalulate_choice(choice)


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
    '''
    displays the menu options
    Return: user's choice
    '''
    print("- " * 12, "MENU ", "- " * 12)
    print("1) Calculate Tuition for All Students")
    print("2) Calculate Tuition for Specific Students")
    print("3) Exit")
    print("- " * 12, "MENU ", "- " * 12)
    choice = int(input("Select an option: "))
    return choice


def evalulate_choice(choice):
    '''
    Validates and evaluates user's choice
    Return: None
    '''
    while choice != 3:
        if choice == 1:
            tc.calc_full_tuition()
            print()
            choice = menu()
            evalulate_choice(choice)
        elif choice == 2:
            stu_num = tc.choose_student()
            tc.calc_single_tuition(stu_num)
            choice = menu()
            evalulate_choice(choice)
        elif choice < 1 or choice > 3:
            choice = input("Invalid entry. Please try again: ")
    print("Program exiting...")

# Call the main
if __name__ == "__main__":
    main()