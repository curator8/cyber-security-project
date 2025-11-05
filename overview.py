# personal programming style 
# use f strings for formatting output
# print() and input()
# example 


# data types in python 

# strings, integers, floats, booleans, lists, tuples, dictionaries, sets

# srtings
name = 'billy'
first_letter = 'billy'[0]
print(f'first letter of name is : {first_letter}')
# integers
age = 10
print(type(age))
# floats
height = 5.9    
print(type(height)) 
# booleans
is_student = True
print(type(is_student))
# lists
characters = ['billy', 'mandy', 'grim']
print(f'characters list: {characters}')

# using for loop to iterate through list 
for character in characters:
    print(f'character: {character}')
    
# utilizing range() to generate a sequence of numbers
for num in range(1, 6):
    print(f'number: {num}')

# tuples
coordinates = (10.0, 20.0)
print(f'coordinates tuple: {coordinates}')
# dictionaries
person = {'name': 'billy', 'age': 10}
print(f'person dictionary: {person}')
# sets
unique_numbers = {1, 2, 3, 4, 5}
print(f'unique numbers set: {unique_numbers}')



#conditional statements

 
input_age = float(input('Enter your age: ').strip())
print(f'your age is, {input_age}!')

if input_age < 18:
    print(f'{input_age} = minor.')


# functions 
def function(): 
    print("hello world") 

function()