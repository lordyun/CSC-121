# Calculating the cost of buying in bulk
# 1-14-25
# CSC121 m1Lab1 - Review
# Michael Choi
'''
ask user how many candles they want to buy
input candles
if candles < 19
    cost = 4.75
elif candles < 49
    cost = 4.50
elif candles < 99
    cost = 4.25
else
    cost = 4.00

total_cost = cost * candles
display total_cost

ask user if they want to run the program again
'''
answer = "yes"
while answer.lower() == "yes":
    candles = int(input("How many candles do you want to buy? "))
    if candles >= 1 and candles <= 19:
        cost = 4.75
    elif candles >= 20 and candles <= 49:
        cost = 4.50
    elif candles >= 50 and candles <= 99:
        cost = 4.25
    elif candles >= 100:
        cost = 4.00
    else:
        cost = 0.00
        print()
        print("Invalid amount. Please try again.")

    total_cost = cost * candles
    print()
    print(f"Number of candles: {candles}")
    print(f"Cost per candle: {cost:.2f}")
    print(f"Total cost: ${total_cost:.2f}.")
    print()
    answer = input("Do you want to run the program again? Answer 'yes' or 'no': ")
print()
print("Program has closed. Goodbye.")
