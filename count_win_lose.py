
print("To calculate your expenses.Please enter all the required information")

number_kilometers=float(input("Please enter how many klilo meteres did you spend today : "))

consumption_100km=float(input("Please enter the vehicle consumption (per 100 K.M) :"))

fuel_price=float(input("Enter the price of fuel :")) 

amount_money=float (input("Enter the total money you took from work today"))

fuel_cost=number_kilometers*consumption_100km/100*fuel_price

commission=amount_money*0.105

maintenance_cost=number_kilometers*0.05

total_cost=commission+maintenance_cost+fuel_cost
profit=amount_money-total_cost

print(f"You drove {number_kilometers} K.M \nYour {consumption_100km} per 100.K.m  \nThe fuel cost is{fuel_cost:.2f}\nThe commissiom was {commission:.2f} \nThe maintenance cost is {maintenance_cost:.2f}  \nYour profit is {profit:.2f}")
print(f"Your cost is :{total_cost:.2f}")
if profit> total_cost:
    print("Good job")
elif profit==total_cost:
    print("You don't achieved any profit")
else:
    print("Today you have something wrong you lose money and not achived any profit")

import datetime
now=datetime.datetime.now()
print("Date and Time :")
print(now.strftime("%Y_%m_%d %H : %M: %S"))
print("thank you for using our program \npowered by Code Flow\nprogrammer: Mohamed wassim tatari")
