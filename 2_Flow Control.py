###Introduction to Python - Nackademin
## Session 2 - Flow Control
## Based on Chapter 2 from Automate the Boring Stuff


#sometimes you only want a part of a code to run if a certain condition is met
#this is what flow control is used for


#Boolean values
#True, False
#can used to determine if conditions are met



#Comparison operators
# == is equal to (note the double ==)
# != is not equal to
# < less than
# <= less than or equal to
# > greater than
# >= greater than or equal to

42 == 42
42 != 42

"string" == "string"
42 == "42"

True == True
False == False
True == False

#booleans have numerical equivalents
#0 is false, 1 is true 
0 == False
1 == False
1 == True
0 == True
2 == True



#Not with boolean operators
not True
not False



#Boolean and comparisons can be mixed
(4 < 5) and (5 < 6)
(4 < 5) and (5 > 6)
(4 < 5) or (5 > 6)





##-------------------------------------------------
## Elements of flow control

#Conditions
#conditions always evaluate down to a True or False

#Blocks of code
#indentation is necessary!
#use four spaces!



#Flow Control Statements
#if statements
# if condition is met, do something
a = 5
if a >= 4:
    print(a)
    

#else statements
# what to do if the if statement condition is not met
a = 3
if a >= 4:
    print(a)
else:
    print(a, "is less than 4")

#elif statements
#if there are two or more different possible conditions that can be met
a = 3
month = "february"
if a >= 4:
    print(a)
elif month == "february":
    print("it's february")

#the statement outputs at the first condition that is met
a = 5
month = "february"
if a >= 4:
    print(a)
elif month == "february":
    print("it's february")
    
#you can add as many of these elif statements as you need/want
#you do not need an else statement as you can see above
#but the else statement will ensure that some output is created regardless of whether or not 
#a condition is fulfilled
#but the order must be kept.  First the if statement, then any eventual elif statements, 
#then an else statement
    


##----------------------------------------------------------------
#Loops

#While loops
#do something while a condition is met
a = 10
while a >= 1:
    print(a)
    a = a - 1

#update the condition, now the while condition is not met as many times
#also note the change, no longer a = a - 1
#python has a shortcut for this a -= 1
#the equivalent for addition also exists, a += 1
a = 10
while a >= 5:
    print(a)
    a -= 1

#now, what happens if the condition never evaluates to true?
a = 10
while a <= 5:
    print(a)
    a += 1
#nothing
    
#but what about if it never evaluates to false?
#it will keep going forever
#click on the console with the mouse to put focus there, then hit ctrl-c on the keyboard 
#to stop a runaway script
a = 10
while a >= 5:
    print(a)
    a += 1

#an annoying loop
name = ''                           
while name != 'your name':          
    print('Please type your name.')
    name = input()                  
print('Thank you!')                 
    


#use break to prevent runaways or to exit a loop when a condition is met
a = 10
while a >= 5:
    print(a)
    a += 1
    if a >= 1000:
        break
   

name = ''                           
while True:          
    print('Please type your name.')
    name = input()
    if name == "your name":
        break
print('Thank you!')                 




#For Loops
#the most important type of loop
               
#i is an indexer, it can be whatever
#range() creates a sequence of numbers from 0 to 6 (or whatever number you choose)                
for i in range(6):
    print(i)


print('My name is')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')


#let's look at range in more detail
range(6)
range(10, 20)
for x in range(10, 20):
    print(x)
#not that python is left inclusive, and right exclusive!!!


range(10, 1, -1)
for y in range(10, 1, -1):
    print(y)
    
#each of these three numbers you put in the brackets of range provide values to arguments
#functions have arguments so that you can specify how you want to use the argument
#range(10, 1, -1) says, create a range of numbers from 10 to 1 by subtracting 1 each time

for u in range(20, 0, -2):
    print(u)
    

#So why does range(6) work?
#because functions have default values for some arguments
#in this case, the "start" argument is set to default to 0 and the "by" argument is set to default to 1
#So this:
range(6)
#is really saying this:
range(0, 6, 1)

#but there is not default for the "stop" argument
for y in range():
    print(y)
#so at least one number must be specified
    





##------------------------------------------------------------------------
##Importing Modules
#all of the functions we've seen so far are part of the standard python library.
#but anybody can write a python function and save it into an online library which other 
#users can then install and use themselves.  
#these other online libraries are called modules.  The functions in the modules can be accessed
#by importing the appropriate module.  
#Some modules are written by the python foundation, the same group that is responsible for the
#standard library we have been using so far.  Other modules are written by regular users.
#a host of modules come pre-installed when you install python on your computer.
#others can be installed manually with pip or conda (or whatever setup you use)
#to get access to these modules in your current python session

#use import then module name
import random
#now to get access to the functions in random, you have to precede the function
#name with random.function()
for i in range(6):
    print(random.randint(1, 10))


#you can also import a single function from a module
from random import randint
#in this case you do not need to precede the function with random.
for i in range(6):
   print(randint(1, 19))


#lastly, you can import modules under an alias
#let's say that you think it is annoying to type out random each time and want to type something shorter
import numpy as np
for i in range(6):
    print(np.random.normal(1))

#now you use the alias rather than random to precede the function
#there are some packages where the alias is standard.  
#Eg pandas is always imported as pd
#numpy as np
#try to follow accepted custom so that others can easily read your code
    



##------------------------------------------
#Task
