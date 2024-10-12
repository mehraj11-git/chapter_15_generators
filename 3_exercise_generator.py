# def a generator function 
# this will take a number as an argument 
# this will return the even numbers

def even_num(n):
    for i in range(1,n+1):
        if i%2==0:
            yield(i)
for n in even_num(20): #<------ if we store this even_num() in variable and then print it,then we cant print it more than one time
    print(n)

# short form
# here we are using step method 
def even_num(s):
    for i in range(2,n+1,2):
        yield(i)
for k in even_num(20):
    print(k)