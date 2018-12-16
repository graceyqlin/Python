def averages():
    try:
        import math
        a = int(input("Enter the first number" ))
        b = int(input("Enter the second number" ))
        method = int(input("Enter the method for the average (1 for arithmetic mean, 2 for geometric mean, or 3 for root-mean-square)"))
        if method == 1:
            print("the arthmetic mean is", format((a+b)/2,'.2f'))
        elif method == 2:
            print("the geometric mean is", format(math.sqrt(a*b),'.2f'))
        elif method == 3:
            print ("the root-mean-square is", format(math.sqrt(0.5*(a**2+b**2)),'.2f'))
        else:print ("error")
    except:
        print("Please enter a number")
        return

averages()