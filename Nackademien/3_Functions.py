## Session 3 - Functions
## Based on Chapter 3 of AtBS


#the purpose of writing custom functions is to prevent the need to duplicate your code. 
#if you find yourself copy and pasting parts of your code, it is time to start thinking about 
#writing a function.  As a general rule of thumb, if you copy and paste more than twice in the same
#script, you should write a function to prevent such duplication.



##Creating functions
#when writing functions, they must first be defined using a def statement
def hello():
    print("Hello")

#after they've been defined they can be called, just like any other function    
hello()


#the above function, hello(), has no parameters.  Nothing is written between the ().
def hello(name):
    print("Hello, " + name)
    
#now we have a new hello function with the parameter, or argument, name
#when we call this function we need to supply the parameter with a values
hello("bob")
#if we don't we will get an error
hello()
#because the function does not know what value to give to the name argument

#if you want to assign a default argument, you can do it in the def call
def hello(name = "please give a name"):
    print("Hello, " + name)
hello()
#but if a name argument is supplied, the default value is ignored
hello("bob")
#you will mostly want to do this if there is a really common value for a certain argument
#remember the default values of the range() function?





##Return values
#the print() function displays something on screen, but it doesn't save anything.
spam = print("Hello")
spam
#functions can be used to return specific values, either based on conditional statements or calculations
#in this case, if you want a value to be given as the result of your function
#use return

def math_func(a = 0, b = 0):
    return a + b
math_func(2, 4)
#these values can then be saved into other variables for later use
x = math_func(2, 4)
x
#any function that does not include a return statement automatically returns a None (blank) value
#just like the print function
def math_func2(a, b):
    a + b
#note that there is no return
x2 = math_func2(1, 2) #so nothing gets saved here. there is no print either so nothing is printed
x2 #so this is blank





##---------------------------------------------------------------
##Local and Global Scope
#parameters and variables defined within a function have local scope. That is, they are available
#in the function only

#on the other hand, variables defined outside of functions have global scope.  That is, they are
#available both to functions and outside of functions
def math_func(num1 = 2, num2 = 4):
    return num1 + num2
num1
#num1 is defined in a function, it is therefore not accessible outside of that function

glob_num = 5
def math_fun(num1, num2):
    return num1 + num2 + glob_num

math_fun(1, 2)
#glob_num is defined in the global environment so it is available both outside of functions and
#within functions

#these are the most important points, but read more about scope in AtBS





##--------------------------------------------------------------------
#Error handling with try and except

def divider(divide_by):
    return 42 / divide_by

divider(12)
#this naturally returns an error because you cannot divide by zero
divider(0)



#try and except allow you to handle these types of problems.  
#with try: the function will try to compute. If it works, the function will output the return
#value and exit the function.
#if there is an error as a result of the computation, the function will look at the except clause
#if it matches the error that the function produced, the except output will be given.
def divider(divide_by):
    try:
        return 42 / divide_by
    except ZeroDivisionError:
        print("Error: can't divide by zero")
        
divider(0)


#But this will still cause us problems:
divider("42")

#so we can add further error types
def divider(divide_by):
    try:
        return 42 / divide_by
    except ZeroDivisionError:
        print("Error: can't divide by zero")
    except TypeError:
        print("Error: must be a number")
        
divider("42")
divider(0)

#this will keep your program from breaking if the wrong input value is given to a function











##---------------------------------------------------------------
##Collatz sequence
def collatz(number):
    if number % 2 == 0:
        print(number / 2)
        return number / 2
    else:
        print(number*3+1)
        return(number*3+1)

print("input a number")
number = int(input())
while number != 1:
    number = collatz(number)






