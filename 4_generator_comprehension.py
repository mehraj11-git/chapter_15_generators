# if u know how to make list comprehension than you can easily make the generator comprehension

# for ex:
square = [i**2 for i in range(1,11)]
print(square)

# this is list comprehension 
# for generator comprehension we have to change the square bracket with paranthesis
square_list= (i**2 for i in range(1,11))
for k in square_list:
    print(k)
for k in square_list:
    print(k)

# it gonna print one time only    
