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


'''
Problem 3
Write a function print_catchphrase() that accepts a string character as a parameter
and prints the catchphrase of the given character as outlined in the table below.

'''

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

