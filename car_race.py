# create the car class
import random 
class Car:
    # create the initializer function
    def __init__(self, make, model, color, driver, max_speed, handling):
        self.make = make
        self.model = model
        self.color =  color
        self.driver = driver
        self.max_speed = max_speed
        self.handling = handling
        self.miles_driven = 0
    def show_car_info(self):
        print(f"The {self.color} {self.make} {self.model} is driven by {self.driver}.")
    def drive_car(self):
        self.miles_driven += random.randint(5, self.max_speed) + self.handling
        return self.miles_driven
        
    def show_stats(self):
        print(f"{self.driver} advanced to the {self.miles_driven} mile marker.")


    def winner(self):  
        print(f"{self.driver} won the race!")
    
    def obstacle(self):
        value = random.randint(0,5)
        if value == 1:
            speed = random.randint(3, 8)
            self.max_speed -= speed
            print(f"Whoops- {self.driver} hit a banana peel and slowed down by {speed}.")
        elif value == 2:
            speed = random.randint(9, 15)
            self.max_speed -= speed
            print(f"Oh no! {self.driver} got distracted by a butterfly and ran off the road, losing {speed}.")
        elif value == 3:
            speed = random.randint(16, 30)
            self.max_speed -= speed
            print(f"Disaster! {self.driver} took a turn too fast and spun out, losing {speed}.")
        else:
            print(f"{self.driver} is gaining speed.")

def main():
    miles_to_win = 100
    # create a car object
    muskCar = Car("Tesla", "S", "white", "Elon Musk", 80, 10)
    # create a second car
    myCar = Car("Ford", "Focus", "black", "Michael Choi", 80, 10)
    # call the instance function show car info
    muskCar.show_car_info()
    myCar.show_car_info()
    print()
    print("The race has begun...")
    print()

    # drive both cars at one time
    milesMusk = 0
    milesMe = 0
    while milesMusk < miles_to_win and milesMe < miles_to_win:
        milesMusk = muskCar.drive_car()
        milesMe = myCar.drive_car()
        if milesMusk < miles_to_win and milesMe < miles_to_win:
            muskCar.show_stats()
            myCar.show_stats()
            print()
        elif milesMusk > miles_to_win:
            muskCar.show_stats()
            print()
            muskCar.winner()
            break
        elif milesMe > miles_to_win:
            muskCar.show_stats()
            myCar.show_stats()
            print()
            myCar.winner()
            break
        elif milesMusk == milesMe:
            muskCar.show_stats()
            myCar.show_stats()
            print()
            print("It's a tie!")
            break
        muskCar.obstacle()
        myCar.obstacle()
        print()
    

if __name__ == "__main__":
    main()