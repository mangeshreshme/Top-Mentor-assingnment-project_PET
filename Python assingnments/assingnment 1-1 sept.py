'''
 Assingnments (1 sept)
Problem no 1-  Using python program calculate DA,HRA ,And Gross Pay
 '''


def calc_groos_pay(basic_pay, da_percent,hra_percentage, ):
    da = basic_pay*da_percent/100
    hra = basic_pay*hra_percentage/100
    gross_pay= basic_pay+da+hra
    return da,hra,gross_pay

basic_pay = float(input("Enter basic Pay :"))
da_percent = float(input("Enter Da Percentage:"))
hra_percentage= float(input("Enter HRA percentage:"))

da,hra,gross = calc_groos_pay(basic_pay, da_percent,hra_percentage)
print("DA=",da)
print("HRA=",hra)
print('Gross pay=',gross)

"""
Problem no 2- calculating monthly income & expence
"""
def calc_exp(rent,food,electricity,phone,cable):
    return rent+food+electricity+phone+cable
def check_saving(income,expenses):
    if income>expenses:
        print('you have saving of RS;',income-expenses)
    elif income<expenses:
        print('you have to barrow RS.',expenses-income)
    else:
        print('No Saving No Borrowing')
income = float(input("Enter Monthly income:"))
rent = float(input('Enter montly rent:'))
food = float(input("enter food Expense:"))
electricity= float(input("Enter electricit bill:"))
phone = float(input('Enter Phone Bill:'))
cable = float(input('Enter cable charges:'))
total_expenses = calc_exp(rent,food,electricity,phone,cable)
print('Total Montly Expenses=',total_expenses)
check_saving(income,total_expenses)
