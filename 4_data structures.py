###Introduction to Python - Nackademin
## Session 4 - Python Data Structures
#Based on Chapters 4 and 5 of AtBS


##Lists
#Lists have multiple, ordered values
#use square brackets [ ] to define a list, and separate values with a comma
L = [1, 2, 3]
L2 = [4, 5, 2, 5]

L
L2


#note, order does not mean any specific numerical or alphabetical order of the items of the list.
#simply that a list always its values in the same order as when they were created, unless
#you specify later to change the order in some way

#lists work with all data types
L_str = ["a", "list", "of", "strings"]
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
#extract from element 1 to element 3
spam[1:3]
#remember, left inclusive, right exclusive!


#if we want the first three items, we can write
spam[0:3]
#or
spam[:3]
spam[1:]

#negative numbers index from the end
spam[-1]
#gets the last element


#if we want the last three elements
spam[-3:]

#
spam[0:3:2]

#if you want to extract non-consecutive elements, you need to use a different (non base-python) data structure
#or define your own custom function.
#here are two possible solutions:
import numpy as np
L_np = np.array(spam)
L_np[[0,2]]

def list_extract(list, a, b):
    return [list[a], list[b]]
list_extract(spam, 0, 2)





##-----------------------------------------------------------
#Working with lists

#using indexes, we can change values of a list
spam
spam[2] = "a bigger rat"
spam



#the length of a list can be found with the len() function
len(L)
len(spam)

#the len() functions counts the length of the object you call the function on.
#this works on other things too, not just lists
len("This is a sentence. The len() argument will count the number of items in the sentence.")


#combining (concatenating) lists
L
spam
L + spam

#repeating lists
L * 5

#deleting values of a list can be done with the del function
spam
del spam[3]
spam



#lists can be created with a specific list() function as well because sometimes typing out
#every value of a list is too tedious.  Imagine if you want a list of 40 items:
L = list(range(10, 50))
L


#other times you may wish to coerce an object in a different data structure to a list, in this case
#the list() function is necessary. 
#for example, a tuple is created with () rather than [] and has some different properties. If we want
#to convert a tuple to a list, we can wrap it in a list() call
my_tuple = ("cat", "dog", 5)
type(my_tuple)

my_tuple[2] = "b"

L2 = list(my_tuple)
L2
type(L2)
L2[2] = "b"
L2


#we'll see this used again further below with the map() function





##---------------------------------------------------------
#Using for loops with lists
#remember this:
for i in range(4):
    print(i)
    
    
#we can do something similar over the elements of a list
#we'll use our trusty spam list
spam = ["Cat", "Bat", "Rat", "Elephant"]
spam
for i in spam:
    print(i)
    
#again, is an indexer, it can be anything
for element in spam:
    print(element)



##-----------------------------------------------------------------
#Methods
#methods are like functions, but they are called on objects. 
#the format is object.method()
#for example, .index() is a method that can be called on a list to determine the position of
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
#not the difference between the above and
spam = ['hello', 'hi', 'howdy', 'heyas']
spam
spam[2] = "bonjour"
spam
#which would replace the third element with bonjour rather than adding an element in the third position

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

#access elements with indexing
T[2]

#but things like append, sort, and assignment do not work
T.append(5)
T.sort()
T[2] = 1






##--------------------------------------------------------------
#Dictionaries
#The third multi-value data type, dictionaries are like lists but they are a collection of 
#key-values pairings.  
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
birthdays
#they are created with curly brackets, key: value, key: value etc.


#getting dictionary information with methods
birthdays.values()
birthdays.keys()
birthdays.items()


#looping over a dictionary prints the keys
for d in birthdays:
    print(d)
    
    
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






    
#---------------------------------------------------------
#Building a list

#three primary techniques:
#for loops

#create a blank list
L = []
L
#then fill it in the loop
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
fun_fib(27)
        

#List comprehension
#a shortcut to creating lists so you don't have to write the full for loop
L = [i for i in range(10)]
L

#is identical to:
L = []
for i in range(10):
    L.append(i)
L



L2 = [i**2 for i in range(10)]
L2
#is identical to:
L2 = []
for i in range(10):
    L2.append(i**2)
L2



L3 = [i + i - 1 if i > 0 else i for i in range(10)]
L3
#is identical to:
L3 = []
for i in range(10):
    if i > 0:
        L3.append(i + i - 1)
    else:
        L3.append(i)
L3

#Comprehensions are very useful because they allow you to write short, neat code.
#But they quickly become difficult to read as statements become more complex

#Dictionary comprehension works too, see here for some examples
# http://cmdlinetips.com/2018/01/5-examples-using-dict-comprehension/




#using all or any
#all - check if list1 contains all elements of list 2
colors
all(elem in ["blue", "red"] for elem in colors)
all(elem in colors for elem in ["blue", "red"])

#any - check if list1 contains any element of list2
any(elem in ["blue", "red"] for elem in colors)
any(elem in colors for elem in ["blue", "red"])



#the same can be applied to lists
"Alice" in birthdays.keys()

any(elem in ["Alice", "Bob"] for elem in birthdays.keys())








###----------------------------------------------------------
## The map function and lambda functions

##
# the map function

##an efficient way to iterate over an object and apply a function to each element
#similar objective to list comprehension, but easier with multiple inputs/more complex functions
fruits = ["apples", "bananas", "oranges"]
len(fruits)

m = map(len, fruits)
m

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


##
#lambda functions

#in the example above I defined a function first, then mapped over it.  But if you are mapping a function
#only one time, you can skip the definition step and define it in the map function itself using 
# a so-called "lambda" function

sum_list_lambda = list(map(lambda x,y: x + y, a, b))
sum_list_lambda

#the benefit? less code, you don't need to define a function that will stay in memory
#the downside? this function is not available for future use. So this technique is only useful
#if you will only use the function once!! If you plan on using this function several times, it is better
#to define it in the normal fashion.


    



