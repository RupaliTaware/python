
def is_prime(num):
       
    for i in range(2, num):        
        
      
            if(num==0 or num==1 or num%i==0):
                print("{} is Not Prime Number" .format(num))
                break
                
            elif(i==num-1):
                print("{} is  Prime Number" .format(num))
                
                 
           
value=input("Enter a number")
value=int(value)
ans=is_prime(value)
