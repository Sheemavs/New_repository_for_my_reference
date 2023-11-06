#1--><OnTrue> if <Condition> else <OnFalse>
var = 0 if 3==3 else 4
print(var)


#2-->
x=67
print("no") if x > 42 else print("yes") if x == 42 else print("maybe")


#3-->
##############################
# Method 1: Single-Line Def
##############################
def f1(x): return str(x * 3) + '!'

print(f1(1))
print(f1('python'))

##############################
# Method 2: Lambda Function
##############################
f2 = lambda x: str(x * 3) + '!'

print(f2(2))
print(f2('shee'))

##############################
# Method 3: exec()
##############################
f3 = "def f(x):\n    return str(x * 3) + '!'"

exec(f3 + '\nprint(f(8))')
exec(f3 + "\nprint(f('opthon'))")

#4-->
for i in range(10): print(i)
s=[j*2 for j in range(4)]
print(s)

#5-->
def creating_gen(index):  
    months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']  
    yield months[index]  
    yield months[index+2]  
next_month = creating_gen(3)  
print(next(next_month), next(next_month))  

#6--> How do you print the summation of all the numbers from 1 to 20
print(sum(range(1,21)))  

#7--> In a function, how do you create a global variable?

global_var=0
def assign_glob():
    global global_var
    global_var=12
def call_glob_val():
    print(global_var)
assign_glob()
call_glob_val()

#8--> Is it possible to construct a Python program that calculates the mean of numbers in a list?

n=int(input("enter how many number"))
l=[]
for i in range(0,n-1):
    element=int(input("enter numer"))
    l.append(element)
mean= sum(l)/n
print(round(mean,2))

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

service_obj=Service()
driver=webdriver.Firefox(service=service_obj)
driver.get("https://paymentcenter.ipccsandbox.com/engagement/")