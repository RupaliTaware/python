def palidrome(my_str):
    l=(len(my_str)-1)
    i=0
    while(i<=l):
        if(my_str[i]==my_str[l-i]):
            i+=1
        else:
            print('Given string {} is Not Palidrome' .format(my_str))
            break
        print('Given string {} is  Palidrome' .format(my_str))
        break


us=input('Enter any String')
palidrome(us)