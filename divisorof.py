
def divisor(num):
    print('The Divisors of {} are---' .format(num))
    for i in range(1,num+1):
        if(num%i==0):
            print(i)
        else:
            continue


nd=int(input('Enter no to find its Divisors'))
divisor(nd)

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





def fibco(n):

     sum=1
     sum_list = [0]
     for i in range(0, n):
        sum_list.append(sum)
        sum=sum+sum_list[i]

     print('The Fabonacci of range{} is' .format(n))
     print(sum_list)

f_no=int(input('enter no of Fibonacci you want'))
fibco(f_no)