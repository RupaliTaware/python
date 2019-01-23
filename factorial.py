def fact_no(num):
         product=1
         if(num==1):
             print('The Factorial of no {} is {}' .format(num,num))
            
         elif(num<0):
             print('Entered No. is invalid ')
            
         else:
             for i in range( 1, (num+1)):
                product=product*i
             return product
    
    
    
value=int(input('Enter the number'))
ans=fact_no(value)
print('The factorial of {} is {}' .format(value,ans))
