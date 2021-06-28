# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 20:14:53 2021

@author: DHIVYADARSSHNI
"""

#Creating an calculator:
    
def addition(num1,num2): #defining Addition function
    return num1+num2

def subtraction(num1,num2): #defining Subtraction function
    return  num1-num2

def multiplication(num1,num2): #defining Mutltiplication function
    return num1*num2

def division(num1,num2): #defining Division function
    return num1/num2

def exponentiation(num1,num2): #defining Exponentiation function
    return num1**num2
condition=True
choice=int(input('''                             
        -----Calculator is opened----- 
          Select any number for operations:
          1.Addition
          2.Subraction)
          3.Multiplication
          4.Division
          5.Exponentiation(only numbers):
                        '''))                               #printing the menu
          
num1=float(input("Enter a valid number or float: "))          
num2=float(input("Enter a valid number or float: "))        #getting the values as input

if choice==1:                                               #checking the condition: if it's 1,then add function implements
        print(num1,'+',num2,'=',addition(num1,num2))
        
    
elif choice==2:                                              #checking the condition: if it's 2,then sub function implements
        print(num1,'-',num2,'=',subtraction(num1,num2))    
    
    
elif choice==3:                                               #checking the condition: if it's 3,then multiply function implements
        print(num1,'*',num2,'=',multiplication(num1, num2))
        
elif choice==4:                                                #checking the condition: if it's 4,then division function implements
        print(num1,'/',num2,'=',division(num1,num2))
    
elif choice==5:                                                #checking the condition: if it's 5,then exponentiation function implements
        print(num1,'**',num2,'=',exponentiation(num1,num2))   
    
else:
        print('Invalid Input')
        

print('     -----Calculator is closed-----')
       

    
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    