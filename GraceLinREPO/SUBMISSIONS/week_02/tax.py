def cal_tax():
    income = input("Please enter your income: ")
    try:
        income = float(income)
        if income<1000:
            tax = income*0.05
        elif income<2000:
            tax = 1000*0.05 + (income-1000)*0.1
        else:
            tax = 1000*0.05 + 1000 * 0.1 + (income-2000)*0.15
        print("The tax owed is", tax)
    
    except:
        print("Please enter a number")

cal_tax()