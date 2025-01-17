# Michael Choi
# 1-17-25
# CSC 121 m1Lab2- Review
# This program

run_again = "yes"
# create the counter to number multiple routes
count = 1
# create a list to store route times
timeList = []
# create a loop so the user can add multiple routes
while run_again.lower()== "yes":
    # get distances and speeds
    miles = float(input(f"Enter the distance for route {count}(miles): "))
    # validation loop
    while miles <= 0: 
        miles = float(input("Invalid entry. Enter a distance greater than 0: "))
    speed = float(input(f"Enter the speed for route {count}(miles/hour): "))
    # validation loop
    while speed <= 0:
        speed = float(input("Invalid entry. Enter a speed greater than 0: "))
    # caculate time in minutes
    time = (miles / speed) * 60 
    # add time to list
    timeList.append(time)
    # if user wants to add another route, the route number will increase
    count += 1
    # ask user if they want to add routes
    run_again = input("Would you like to enter more routes? (Yes/No): ")
# Show user which route is fastest
print (f"Route {timeList.index(min(timeList)) + 1} is the fastest route: {min(timeList):.2f} minutes.")

