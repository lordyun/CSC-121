# Michael Choi
# 2-7-25
# CSC 121 - M5Project
# this program reads and writes files to get the grades and display grade/tuition of students
# I use chatgpt for the read_csv and get_grade functions. I used it other places to help with ideas, but not a lot and i don't remember exactly where

import m5pro_functions as pro

def main():
    x = pro.read_csv()
    pro.display_info()
    choice = pro.menu()
    pro.evaluate_choice(choice, x)
if __name__ == "__main__":
    main()