def calc_dollars(**coins):
    dollars = 0
    for name, coin in coins.items():
       if (name == 'pennies'):
           dollars += coin/100 
       elif (name == 'nickels'):
           dollars += coin/5 
       elif (name == 'dimes'):
           dollars += coin/10 
       elif (name == 'quarters'):
           dollars += coin/25 
    print(dollars)

calc_dollars(pennies=342, nickels=9, dimes=32, quarters=4)