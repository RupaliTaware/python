
def divisor(num):
    print('The Divisors of {} are---' .format(num))
    for i in range(1,num+1):
        if(num%i==0):
            print(i)
        else:
            continue


nd=int(input('Enter no to find its Divisors'))
divisor(nd)







