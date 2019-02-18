###Introduction to Python - Nackademin
## Session 1 - The Basics


###
### Use # to write comments
### These are probably the most important thing in your code
### Help others and your future self to understand your code
### Comment too much rather than too little, you'll thank yourself later



#-----------------------------------------------

##Expressions
#Expressions take input and evaluate to a single value
2 + 2
2 - 2

2 * 4
4 / 2
2 ** 4


#modular division
21 % 4
21 // 4




#order of operations
2 + 3 * 6
(2 + 3) * 6


#syntax errors
5 +
#There are many other types of error message, we'll come across others as we work through the scripts




##Data Types
#Integers (whole numbers)
#eg 1, 2, 3, -1 etc.
type(1)

#Float (decimals)
# eg 1.5, 3,7, 4.35364262, 2.0
type(4.35364262)
type(3.0)

#Strings (text)
#text wrapped in " or '
#eg "this is a string" 'so is this'
type("this is a string")
type('so is this')



##String concatenation
#combine two strings
"two" + "strings"

#this is a string
"42"
type("42")

#can't conctenate different data types - causes an error
"two" + 42

#but this works
"two" + "42"




##coercion
#to make "two" + 42 work, you need to change the format of the 42
str(42)
"two" + str(42)

#other coercions
str(42)
float(3)
int("42")

#int can be used for rounding down a float
int(7.7)


##string plus number doesn't work, but multiplication does!
"mystring" * 5
#but this doesn't work
"mystring" * "anotherstring"
#nor this:
"mystring" * 5.0



#----------------------------------------------------------
## Variables and assignment

#think of them as boxes in which you can place values
#initialize a variable with assignment
my = 5
var = 10

#after you have assigned them, you can use them in expressions
my * var

#you can save results to a variable as well
a = my * var
a

#this works with strings or floats as well
string_var = "coffee"
float_var = 3.5

#then the same rules apply as above
string_var * my
string_var * float_var

#variables can be overwritten
string_var = "no more coffee"

##Variable names
#one word only
#numbers allowed, but can't start with numbers
#_ allowed, but no other characters

#variable name style
#some use camel case naming
myVar = "this is a variable name in camel style"
#This is why it is called an iPhone and not an IPhone or iphone!!

#others snake case
my_var = "this is a variable name in snake style"

#variable names are case sensitive
#Doesn't really matter which style you choose, just pick one and stick to it
#google has style guides for many programming languages. You can choose to follow 
#from there if you wish.  


## The Print function
print("hello world!")
#seems unnecessary now, can be useful for other things.



###---------------------------------------------------------
##Interactive use vs programming

#What we've done so far is called interactive use
#Interactive use is when you evaluate and examine
#great for learning and when creating new programs
#can go through code one line at a a time, etc.

#but eventually you will want to run the whole script
#save the script as a python file, now you've created a program
#programming is edit, compile, run
#write the first program.py file
#run in idle
#then run in command line
#name variable is gone in command line after it has run








###---------------------------------------------------------






##Task

a = 5
b = 10
c = 7
x = (a + b) * b / c

print("Adding", a, "and", b, "then multiplying by", b, "then dividing by", c,  "gives", x, ".  Rounded down to the nearest whole number gives", int(x), ".")


