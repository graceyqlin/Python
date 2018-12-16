def tip():
    price = input("Enter the price of a meal:") 
    try:
        price = float(price)
    except:
        print("please enter a number")
        return
    
    tip = float(price) * 0.16
    total = (float(price) + tip)

    print("A 16% tip would be ", format(tip,'.2f'))
    print("The total including tip would be ", format(total,'.2f'))      
    
               

tip()