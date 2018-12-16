def palindrome():
    name = input("Please enter your first name: ")
    cp = name.lower()
    name = list(name.lower())
    rev = []
    
    while name:
        rev.append(name.pop())
    reverse = ''.join(rev)
    reverse_final = reverse[0].upper() + reverse[1:]
    print(reverse_final)
    
    
    if reverse == cp:
        print("Palindrome!")
        
palindrome()