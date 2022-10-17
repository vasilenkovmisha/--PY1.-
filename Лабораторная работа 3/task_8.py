money_capital = 10000
salary = 5000
spend = 6000
increase = 1.05
month = 0

delta = salary - spend * increase
while money_capital - spend >=0:
    money_capital -= spend
    money_capital += salary
    spend *= increase
    month += 1

print(month)
