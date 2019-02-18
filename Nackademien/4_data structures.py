## Session 4 - Python Data Structures
#Based on Chapters 4 and 5 of AtBS


##Lists
#Lists have multiple, ordered values
#use square brackets [ ] to define a list, and separate values with a comma
L = [1, 2, 3]
L2 = [4, 5, 2, 5]
#note, order does not mean any specific numerical or alphabetical order of the items of the list.
#just that the list always keeps these values in the same order as when they were created, unless
#you specify later to change the order in some way

#lists work with all data types
L_str = ["a", "list", "of", "string"]
L_str

#you can mix data types
L3 = [1, 2, "String"]
L3

#and lists can contain lists
L4 = [[1, 2, 3], [4, 5, 6 ]]
L4



##-----------------------------------------------
#Accessing specific values of lists
#lists are indexed, that is in this list:
L = ["a", "b", "c"]
# we can consider each value as the first, second, third value of the list
#but, perhaps confusingly, indexing in python starts with 0.
#so to extract a certain value from the list, we make use of square brackets again, and start with 0
#for the first item
L[0]
L[1]
L[2]

spam = ["Cat", "Bat", "Rat", "Elephant"]
spam[2]

#to extract multiple elements, we use the : operator within brackets

spam[1:3]
#remember, left inclusive, right exclusive!

#if we want the first three items, we can write
spam[0:3]
#or
spam[:3]

#negative numbers index from the end
spam[-1]
#gets the last element


#if we want the last three elements
spam[-3:]




##-----------------------------------------------------------
#Working with lists

#using indexes, we can change values of alist
spam
spam[2] = "a bigger rat"
spam


#the length of a list can be found with the len() function
len(L)
len(spam)

#the len() argument counts the length of the object you call the function on.
#this works on other things too, not just lists
len("This is a sentence. The len() argument will count the number of items in the sentence.")


#combining (concatenating) lists
L + spam

#repeating lists
L * 5

#deleting values of a list can be done with the del function
spam
del spam[3]
spam

#lists can be created with the list() function as well because sometimes typing out
#every value of a list is too tedious.  Imagine if you want a list of 100 items
L = list(range(10, 50))
L

#this works with other data types too
L2 = list(("cat", "dog", 5))
L2

#the list() function coerces an object into a list





##---------------------------------------------------------
#Using for loops with lists
#remeber this:
for i in range(4):
    print(i)
    
#we can do something similar over the range of a list

L = list(range(10, 40))
L

for i in L:
    print(i)
    
for i in L2:
    print(i)
    


##-----------------------------------------------------------------
#Methods
#methods are like functions, but they are called on objects. 
#the format is object.method()
#for example, index() is a method that can be called on a list to determine the position of
# a specific input

spam = ['hello', 'hi', 'howdy', 'heyas']
spam.index("hi")

#you'll get an error if you try to get the index for an item that does not exist
spam.index("is this in the list?")


#items can be added to the list with .append()
spam.append("hej")
spam
spam.index("hej")

#and insert lets you specify where in the list a new item goes
spam.insert(2, "bonjour")
spam

#you can remove specific values without knowing the index number
spam.remove("bonjour")
spam

#and you can sort with .sort()
#alphabetic order
spam.sort()
spam

#numerical order if numbers
L = [4,3,5,1,4,2]
L.sort()
L

#but you can't sort if mixed data types
L = ["string", 2, 1, "text"]
L.sort()




##--------------------------------------------------------------
#Tuples
#Tuples are important to python and are often used for return values of functions
#they are like lists, but they cannot be edited afterwards. 
#We say that they are immutable

#create a tuple with ()
T = (1, 2, 3)

#things like append and sort do not work
T.append(5)
T.sort()





##--------------------------------------------------------------
#Dictionaries
#The third multi-value data type, dictionaries are like lists but they are a collection of 
#key-values pairings.  
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}



#getting dictionary information with methods
birthdays.values()
birthdays.keys()
birthdays.items()


#looping over a dictionary prints the keys
for d in birthdays:
    print(d)
    
for k, v in birthdays:
    print(k, v)
    
#to get values you need to loop over the method
for v in birthdays.values():
    print(v)

#to get both, use items
for i in birthdays.items():
    print(i)
    
for k, v in birthdays.items():
    print(k, v)
    



##-----------------------------------------------------------
# Checking contents of lists and dictionaries
#to check whether an entry exists in a list or dictionary, there are the in and not in operators

#Let's say we have a list
colors = ["blue", "red", "green"]
"pink" in colors
"red" in colors
"pink" not in colors


#testing for multiple matches
#using and, or
"blue" and "red" in colors
"blue" and "pink" in colors
"blue" or "pink" in colors


#using all or any
#all - check if list1 contains all elements of list 2
all(elem in ["blue", "red"] for elem in colors)
all(elem in colors for elem in ["blue", "red"])

#any - check if list1 contains any element of list2
any(elem in ["blue", "red"] for elem in colors)
any(elem in colors for elem in ["blue", "red"])



#the same can be applied to lists
"Alice" in birthdays.keys()

any(elem in ["Alice", "Bob"] for elem in birthdays.keys())








    
#---------------------------------------------------------
#Building a list
#the list() function that I showed you above is a way to coerce a pre-existing object into a list

#two primary techniques:
#for loops

#create a blank list
L = []
for i in range(10):
    L.append(i)
L

#naturally, this can get more complicated
L = []
for i in range(10):
    L.append(i**2)
L

#each list item as the sum of i and i - 1
L = []
for i in range(10):
    if i > 0:
        L.append(i + i-1)
    else:
        L.append(i)
L 


#fibonacci sequence 
def fun_fib(n):
    a = 1
    b = 1
    F = [a]
    for i in range(n):
        F.append(b)
        b = b + a
        a = F[i + 1]
    return F

fun_fib(10)
        

#List comprehension
#a shortcut to creating lists so you don't have to write the full for loop
L = [i for i in range(10)]
L

L2 = [i**2 for i in range(10)]
L2


L3 = [i + i - 1 if i > 0 else i for i in range(10)]
L3


#Dictionary comprehension works too, here are some examples
# http://cmdlinetips.com/2018/01/5-examples-using-dict-comprehension/



###----------------------------------------------------------
## The map function and lambda functions

##an efficient way to iterate over an object and apply a function to each element
#similar objective to list comprehension, but easier with multiple inputs/more complex functions
fruits = ["apples", "bananas", "oranges"]
len_fruits = list(map(len, fruits))
len_fruits
#applies the function len to each element of the list fruits
#you have to wrap a list() around the map function (or set, whatever data structure you want as an output)

#the equivalent to this list comprehension
len_fruits_comp = [len(x) for x in fruits]
len_fruits_comp

#which is equivalent to this for loop
len_fruits_loop = []
for x in fruits:
    len_fruits_loop.append(len(x))
len_fruits_loop

#the advantage of map is that you can apply more complex functions easier, for example with multiple inpouts
#say you want to add the elements of two lists
a = [1, 2, 3]
b = [4, 5, 6]

#putting a plus sign between will concatenate the lists:
a + b
#but that's not what you want
#you want
a[0] + b[0]
a[1] + b[1]
a[2] + b[2]


def list_sum(x, y):
    return x + y
sum_list = list(map(list_sum, a, b))
sum_list

#in the example above I defined a function first, then mapped over it.  But if you are mapping a function
#only one time, you can skip the definition step and define it in the map function itself using 
# a so-called "lambda" function

sum_list_lambda = list(map(lambda x,y: x + y, a, b))
sum_list_lambda
#the benefit? less code, you don't need to define a function that will stay in memory
#the downside? this function is not available for future use. So this technique is only useful
#if you will only use it once!! If you plan on using this function several times, it is better
#to define it in the normal fashion.


    



