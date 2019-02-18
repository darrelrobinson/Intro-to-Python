## Flow Control - Task

#Write code that prints Hello if 1 is stored in spam, 
#prints Howdy if 2 is stored in spam, 
#and prints Greetings! if anything else is stored in spam.


## Solution
#1
spam = 3
if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greetings!")    



#2
for i in range(10):
    print(i)
