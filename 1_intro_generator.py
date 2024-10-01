# generators are iterator
# to understand Generator we must have the understanding of iterable and iterators 
# iterable : 
# An iterable is an object in Python that you can loop over, meaning you can access its elements one by one.

# Examples of Iterable Objects:
List_1 = [1, 2, 3, 4]
String_2= "hello"
Tuple_3= (1, 2, 3)
Dict_4= {"a": 1, "b": 2}
Set_5= {1, 2, 3}
# How Does an Iterable Work?
# When you use an iterable object in a loop (like a for loop), 
# Python internally calls the iter() function, which returns an iterator for that iterable.
#  Then, the loop repeatedly calls the next() function to get each element one by one.

# iterator :
# An iterator is an object that has methods to iterate over the elements.
# When you create an iterator from an iterable (through the iter() function),
#  you can use it to get elements one by one using the next() function.

# Example:

my_list = [1, 2, 3, 4]
my_iter = iter(my_list)

print(next(my_iter))  # 1
print(next(my_iter))  # 2
print(next(my_iter))  # 3
print(next(my_iter))  # 4

for num in map(lambda a :a**2,my_list):
    print(num)

# A generator in Python is a special type of iterable that allows you to iterate
#  over data without storing the entire sequence in memory.
#  Generators are created using functions with the yield statement instead of return.
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()

print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
# In this example, my_generator() is a generator function.
#  When next(gen) is called, it runs the function until it hits a yield, 
# which returns the value and pauses the function, 
# ready to continue from where it left off the next time next() is called.