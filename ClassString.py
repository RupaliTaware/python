class string_oprate:
    
    def __init__(self):
        
          self.enter=input(str("Enter  your  string \n "))
        
    
        
    def print_string(self):
        print('Your string  was \n {}' .format(self.enter))
        
    def upper_string(self):
         self.upper= (self.enter).upper()
         print('Your String is Upper case \n {}' .format(self.upper))
         
    def removedigit_string(self):
          self.string_list= list(self.enter)
          i=0
          
          while(i<len(self.string_list)):
                 
                 chek = ['0','1','2','3','4','5','6','7','8','9']
                 for n in chek :
                     if (self.string_list[i]==n):    
                                 self.string_list.pop(i)
                     else:
                         pass
                     
                 i+=1
          self.withoutdigit= "".join(self.string_list) 
          print('Your string have remove all the digits as \n {}' .format (self.withoutdigit))
          

mystring=string_oprate()
       
mystring.print_string()
mystring.upper_string()
mystring.removedigit_string()

       
