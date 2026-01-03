# This will show you how many built-in exceptions are there in python
Error = dir(locals()['__builtins__'])
print(Error)
print(len(Error)) 

# Division by zero exception ( That mean it cant be divided by zero )
try:
    a = 5 / 0 
except ZeroDivisionError as e:
    print("Error: Division by zero is not allowed.", e)
    
# Name error exception ( when variable is not defined )
try:
    print(undefined_variable)
except NameError as e:
    print("Error: Variable is not defined.", e)

# value error exception ( when wrong datatype is provided )
try:
    num = int("abc")
except ValueError as e:
    print("Error: Invalid literal for int().", e)
    
# index error exception ( when index is out of range )
try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError as e:
    print("Error: List index out of range.", e)
    
# key error exception ( when key is not found in dictionary )
try:
    my_dict = {'a': 1, 'b': 2}
    print(my_dict['c'])
except KeyError as e:
    print("Error: Key not found in dictionary.", e)
# attribute error exception ( when attribute is not found )
try:
    num = 5
    num.append(10)
except AttributeError as e:
    print("Error: Attribute not found.", e)
finally:
    print("Exception handling demonstration completed.")