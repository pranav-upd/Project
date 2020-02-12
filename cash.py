from cs50 import get_float
#..
change = 0
cents = 0
quarters = 0
dimes = 0
nickels = 0
pennies = 0
coins = 0
#..
while change <= 0:
    change = get_float("Change owed: ")
#..
change = round(change, 2)
change = change * 100
cents = change
quarters = int(cents/25)
cents = cents - (quarters*25)
dimes = int(cents/10)
cents = cents - (dimes*10)
nickels = int(cents/5)
cents = cents - (nickels*5)
pennies = cents
coins = quarters + dimes + nickels + pennies
print(coins)