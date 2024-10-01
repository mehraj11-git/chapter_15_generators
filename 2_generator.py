# create the first generator with generator func 
# generator function 

# def num(a):
#  for i in range(11):
#   print(i)

# print(num(10))

# now we make generator 
# we have to change the print with yield

def nums(a):
    for i in range(1,11):
         yield(i)

numbers = nums(10)     # 1
for num in numbers:
    print(num)
 
for num in numbers:
    print(num)
    # look here i did loop for two time but it print only one time
    # this is how generator works
    # if we change the variable(1) into list we can do loop more than one time   

    
