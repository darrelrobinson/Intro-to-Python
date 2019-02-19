###Introduction to Python - Nackademin
## Session 2 - Flow Control
## Based on Chapter 2 from Automate the Boring Stuff


#sometimes you only want a code section to run if a certain condition is met
#this is what flow control is used for.
#flow control allows you to specify things like:
#if a condition is true do something
#if a condition is fales do something else



#Boolean values
#True, False
#are used to determine if conditions are met.
#flow control statements evaluate to boolean values.





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
42 == "42" #be careful of data types, these may look the same but they are not
42 == 42.0
42 == 42.00000000001
#a word of caution, even though 42 == 42.0 evaluates to True, in most cases floats are stored 
#with a decimal followed by a long line of 0s ending with a 1
#so you should always avoid writing equality statements (==, !=) with floats.



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

int(True)
int(False)



#Not with boolean operators
not True
not False


#is and is not
True is True
False is False
False is not False
#work much the same as == and !=
#these are typically recommended over == and != in the case of testing for missing values or None values





#Multiple conditions
(4 < 5) and (5 < 6)
(4 < 5) and (5 > 6)
(4 < 5) or (5 > 6)





##-------------------------------------------------
## Elements of flow control

#Conditions
#conditions always evaluate down to a True or False

#Code is written in blocks
#indentation is necessary!
#use four spaces rather than a tab!



#Flow Control Statements
#if statements
# if condition is met, do something
a = 3

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
#equivalents for addition, multiplication, division also exist, a += 1, a *= 10, a /= 2
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
#click on the console with the mouse to put focus there, then hit ctrl-c on the keyboard to stop a runaway script
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
               
#i is a common placeholder for an indexer, but it can be whatever you want
#range() creates a sequence of numbers from 0 to 6 (or whatever number you choose)                
for i in range(6):
    print(i)
    
    
for x in range(6):
    print(x)
    
for boo in range(10):
    print(boo)



#let's look at range in more detail
range(6)
range(10, 20)
for x in range(10, 20):
    print(x)
#not that python is left inclusive, and right exclusive!!!


range(10, 1, -1)
for y in range(10, 1, -1):
    print(y)
    

#each of these three numbers you put in the brackets of range() provide values to arguments
#functions have arguments so that you can specify how you want to use the function
#range(10, 1, -1) says, create a range of numbers from 10 to 1 by subtracting 1 each time
#range(1, 10, 1) says, create a range of numbers from 1 to 10 by adding 1 each time

#help from functions can be accessed with a ?
?range

for u in range(20, 0, -2):
    print(u)
    

#So why does range(6) work?
#because functions have default values for some arguments
#in this case, the "start" argument is set to default to 0 and the "step" argument is set to default to 1
#So this:
range(6)
#is really saying this:
range(0, 6, 1)

#but there is not default for the "stop" argument
for y in range():
    print(y)
    
#so at least one number must be specified


#all functions have help files
?print

#let's play with some of the arguments for print
#there is a sep argument that defauls to ' ' and an end argument that defaults to "\n"
#\n is computer speak for new line
for y in range(10):
    print(y)
    
for y in range(10):
    print(y, end = " ")

for y in range(10):
    print(y, end = "-")

for y in range(10):
    print(y, y, sep = "-", end = " ")




##------------------------------------------------------------------------
##Importing Modules
#all of the functions we've seen so far are part of the standard python library.
#but anybody can write a python function and save it to an online library which other 
#users can then install and use themselves.  
#these other online libraries are called modules.  The functions in these modules can be accessed
#by first installing and then importing the appropriate module.  You only need to install the module
#to your computer once, but you will need to import the module for each script in which you wish
#to use the functions of the module.
    
#Some modules are written by the python foundation, the same group that is responsible for the
#standard library we have been using so far.  Other modules are written by regular users.
#a host of modules come pre-installed when you install python on your computer.
#others can be installed manually with pip or conda (or whatever setup you use).
    
    
#to get access to these modules in your current python session
#use import then module name
import random
#now to get access to the functions in random, you have to precede the function
#name with random.
for i in range(6):
    print(random.randint(1, 10))

?random.randint


#you can also import a single function from a module
from random import randint
#this loads the function into the namespace which means that you do not need to precede the function 
#with random.
for i in range(6):
   print(randint(1, 19))


#lastly, you can import modules under an alias
#let's say that you think it is annoying to type out random each time and want to type something shorter
import random as ran
#now you access the randint function by preceding with ran.
for i in range(6):
    print(ran.randint(1, 19))

#there are some common customs, eg numpy is always imported as np, and pandas are always imported as pd
#try to follow accepted custom so that others can easily read your code
    



##------------------------------------------
#Task
