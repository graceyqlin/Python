def gas():
    gallons = input("Enter a number of gallons of gasoline: ")
    try:
        liters = float(gallons) * 3.7854
        barrels = float(gallons)/19.5
        price = float(gallons)*3.65
        print("Equivalent number of liters is %.4f"%liters)
        print("Number of barrels of oil required to produce is %.3f"%barrels)
        print("Price in U.S. dollars is %.2f"%price)
        
    except:
        print("Please enter a number")
        return
    
gas()