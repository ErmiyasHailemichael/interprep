'''
Problem 1: Reverse Sentence
Write a function reverse_sentence() that takes in a string sentence and returns the sentence with 
the order of the words reversed. The sentence will contain only alphabetic characters and spaces to
 separate the words. If there is only one word in the sentence, the function should return the original string.
'''

'''
Problem 2: Goldilocks Number
In the extended universe of fictional bears, Goldilocks finds an enticing list of numbers 
in the Three Bears' house. She doesn't want to take a number that's too high or too low
 - she wants a number that's juuust right. Write a function goldilocks_approved() 
 that takes in the list of distinct positive integers nums and returns any number from the 
list that is neither the minimum nor the maximum value in the array, or -1 if there is no such number.
'''


'''
Problem 4: Sum of Digits
Write a function sum_of_digits() that accepts an integer num and returns the sum of num's digits.
'''
def sum_of_digits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num = num // 10
    return sum

num = 423
print(sum_of_digits(num))

