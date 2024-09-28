
'''
    Standard Problem Set Version 1

'''
'''
Problem 1: Hundred Acre Wood
Write a function welcome()
that prints the string "Welcome to The Hundred Acre Wood!".
'''
def welcome():
    print("Welcome to The Hundred Acre Wood!")
welcome()

'''
Problem 2: Greeting
Write a function greeting() that accepts a single parameter,a string name, 
and prints the string 
"Welcome to The Hundred Acre Wood <name>! My name is Christopher Robin."

'''
name = 'Ermiyas'

def greeting(name):
    print('Welcome to the Hundred Acre wood '+name+'! My name is Christopher Robin')
greeting(name)


'''
Problem 3
Write a function print_catchphrase() that accepts a string character as a parameter
and prints the catchphrase of the given character as outlined in the table below.
'''
# what is the difference between print and return in python?
# when to use print? when to use return


character = 'Eeyore'

def print_catchphrase():
    if character == 'Pooh':
       print('Oh bother!')
    elif character == 'Tigger':
        print ('TTFN: Ta-ta for now!')
    elif character == 'Eeyore':
        print('Thanks for noticing me')
    elif character == 'Christopher Robin':
        print( 'Silly old bear')
    else:
        print('Sorry! I do not know' + character + 'catchphrase')
print_catchphrase()

'''
Problem 4: Return Item
Implement a function get_item() that accepts a 0-indexed list items and a non-negative integer x 
and returns the element at index x in items. If x is not a valid index of items, return None.

def get_item(items, x):
	pass
'''
# U- understand P- plan I - implement
def get_item(items,x):
    if x < 0 or x >= len(items):
        return None
    else:
        return items[x]
    
items = ["piglet", "pooh", "roo", "rabbit"]
x = -1
print(get_item(items,x))

'''
Problem 5: Total Honey
Winnie the Pooh wants to know how much honey he has. Write a function sum_honey()
 that accepts a list of integers hunny_jars and returns the sum of all elements 
 in the list. Do not use the built-in function sum().

'''
# u - 

def sum_honey(hunny_jars):
    num = 0
    for num_jar  in hunny_jars:
        num = num + num_jar
    return num
hunny_jars = [10, 3, 5, 5]
print(sum_honey(hunny_jars))

hunny_jars = []
print(sum_honey(hunny_jars))

'''
Problem 6: Double Trouble
Help Winnie the Pooh double his honey! Write a function doubled() that accepts a list of integers hunny_jars 
as a parameter and multiplies each element in the list by two. Return the doubled list.
'''
def doubled(hunny_jars):
    num = []
    for num_jar in hunny_jars:
        num .append(2 * num_jar)
    return num
hunny_jars = [1, 2, 3]
print(doubled(hunny_jars))
'''
p - 7
Winnie the Pooh and his friends are playing a game called Poohsticks where 
they drop sticks in a stream and race them. They time how long it takes 
each player's stick to float under Poohsticks Bridge to score each round.

Write a function count_less_than() to help Pooh and his friends determine how many players 
should move on to the next round of Poohsticks. count_less_than() should accept a list of 
integers race_times and an integer threshold and return the number of race times less than threshold

understand - 
- determine the amount players
plan - 
- variable 
- 
implement -

'''
def count_less_than(race_times, threshold):
    count = 0
    for time in race_times:
        if time < threshold:
            count += 1
    return count
race_times = [1, 2, 3, 4, 5, 6]
print(count_less_than(race_times,3))

'''
Problem 8: Pooh's To Do's
Write a function print_todo_list() that accepts a list of strings named tasks.
The function should then number and print each task on a new line using the format:

Pooh's To Dos:
1. Task 1
2. Task 2
'''



'''
Problem 9: Pairs
Rabbit is very particular about his belongings and wants to own an even number of each thing he owns. Write a function can_pair() that accepts a list of integers item_quantities. Return True if each number in item_quantities is even. Return False otherwise.

def can_pair(item_quantities):
	pass
'''

'''
Problem 10: Split Haycorns
Piglet's has collected a big pile of his favorite food, haycorns, and wants to split them evenly amongst his friends. Write a function split_haycorns() to help Piglet determine the number of ways he can split his haycorns into even groups. split_haycorns() accepts a positive integer quantity as a parameter and returns a list of all divisors of quantity.

def split_haycorns(quantity):
	pass
'''

'''
Problem 11: T-I-Double Guh-ER
Signs in the Hundred Acre Wood have been losing letters as Tigger bounces around stealing any letters he needs to spell out his name. Write a function tiggerfy() that accepts a string s, and returns a new string with the letters t, i, g, e, and r from it.

def tiggerfy(s):
	pass
'''

'''
Problem 12: Thistle Hunt
Pooh, Piglet, and Roo are looking for thistles to gift their friend Eeyore. Write a function locate_thistles() that takes in a list of strings items and returns a list of the indices of any elements with value "thistle". The indices in the resulting list should be ordered from least to greatest.

def locate_thistles(items):
	pass
'''

'''
----------------------------------------------
   Standard Problem Set Version 2               |
                                                |
----------------------------------------------  |
'''

'''
Problem 1: Batman
Write a function batman() that prints the string "I am vengeance. I am the night. I am Batman!".

def batman():
	pass
'''

'''

'''