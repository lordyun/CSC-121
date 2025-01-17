# Michael Choi
# 1-16-25
# M2LAB 
# using functions to simulate shopping 

# create a function that returns a string if the string is in a list of avaible items
# create a function that asks the user how many of that item they would like to purchase
# create a function that gets the cost of item
# calculate and display the total cost for all items

# create main functin
def main():
    print("Welcome to Cat-Co!")
    answer = "yes"
    totalCost = 0
    while answer.lower() == "yes":
        item = searchItem()
        quantity = int(input("How many of this item would you like to purchase? "))
        itemCost = getItemCost(item, quantity)
        totalCost += itemCost
        answer = input("Do you want to add more items? Answer 'Yes' or 'No': ")
    display(totalCost)
      
def searchItem():    
    item = input("What item would you like to purchase? ")
    answer = findString(item)
    if answer == True:
        print("This item is available!")
        return item
    else:
        print("This item is not available, please search again.")
        searchItem()
    

# create function to determine if item exists
def findString(x):
    # function takes in one string, if that string exists in a list, return true, otherwise return false
    itemList = ["Cat Food", "Collar", "Catnip", "Bed", "Brush"]
    if x in itemList:
        return True
    else:
        return False

def getItemCost(item, quantity):
    # function takes in an item as a string and a quantity as an integer to calculate and return the cost of the whole purchase using a dictionary
    costDict = {"Cat Food": 17.99, "Collar": 6.79, "Catnip": 13.99, "Bed": 14.50, "Brush": 7.99}
    cost = costDict[item]
    totalCost = cost * quantity
    return totalCost

def display(totalCost):
    print(f"The total cost of your item(s) is ${totalCost:.2f}.")

# call main
if __name__ == "__main__": 
    main()
