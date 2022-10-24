# Write your tests here!
from optimal_change import optimal_change

print("1:", optimal_change(62.13, 100) == "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies.")

print("2:", optimal_change(31.51, 50) == "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies.")

print('3:', optimal_change(99, 100) ==  'The optimal change for an item that costs $99 with an amount paid of $100 is 1 $1 bill.')

print('4:', optimal_change(.75, 1) == 'The optimal change for an item that costs $0.75 with an amount paid of $1 is 1 quarter.')

print('5:', optimal_change(0, 10000) == 'The optimal change for an item that costs $0 with an amount paid of $10000 is 100 $100 bills.')

print('6:', optimal_change(1.24, 100) == 'The optimal change for an item that costs $1.24 with an amount paid of $100 is 1 $50 bill, 2 $20 bills, 1 $5 bill, 3 $1 bills, 3 quarters, and 1 penny.')

print('7:', optimal_change(49.99, 100) == 'The optimal change for an item that costs $49.99 with an amount paid of $100 is 1 $50 bill, and 1 penny.')

print('8:', optimal_change(100, 100) == 'The optimal change for an item that costs 100 with an amount paid of 100 is no change is required.')

print('9:',  optimal_change(101, 100) == 'You did not pay enough for the Item!')

print('10:', optimal_change(0, 0) == "The optimal change for an item that costs 0 with an amount paid of 0 is no change is required.")

print('11:', optimal_change(9.91, 10.90) == 'The optimal change for an item that costs $9.91 with an amount paid of $10.9 is 3 quarters, 2 dimes, and 4 pennies.')

print('12:', optimal_change(9.91, 10) == 'The optimal change for an item that costs $9.91 with an amount paid of $10 is 1 nickel, and 4 pennies.')

print('13:', optimal_change('54', .67)== 'invalid input')

print('14:', optimal_change(-1, 4) == 'Invalid Input')

print('15:', optimal_change(1.37, -4) == 'You did not pay enough for the Item!')

print(optimal_change(54.45, 600))
print(optimal_change(56, 987))