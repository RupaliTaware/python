def table(num):
    print("Table of {}" .format(num))
    for a in range(1,11):
        print( a*num)
        
value=int(input("Enter No"))
table(value)
