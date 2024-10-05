'''
Problem 1: Post Format Validator
You are managing a social media platform and need to ensure that posts are properly formatted. 
Each post must have balanced and correctly nested tags, such as () for mentions, 
[] for hashtags, and {} for links. You are given a string representing a post's content, 
and your task is to determine if the tags in the post are correctly formatted.

A post is considered valid if:

Every opening tag has a corresponding closing tag of the same type.
Tags are closed in the correct order.
def is_valid_post_format(posts):
  pass
'''

'''
On your platform, comments on posts are displayed in the order they are received. 
However, for a special feature, you need to reverse the order of comments before displaying them.
 Given a queue of comments represented as a list of strings, reverse the order using a stack.

def reverse_comments_queue(comments):
  pass
'''

def reverse_comments_queue(comments):
    reverse = []
    
    while comments:
        updated_reverse = comments.pop()
        reverse.append(updated_reverse)

    return reverse

print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))


'''
Problem 3: Check Symmetry in Post Titles
As part of a new feature on your social media platform, you want to highlight post titles that are symmetrical, meaning they read the same forwards and backwards when ignoring spaces, punctuation, and case. Given a post title as a string,
 use a new algorithmic technique the two-pointer method to determine if the title is symmetrical.
'''

def is_symmetrical_title(title):
    left, right = 0, len(title)-1

    while left<right:
        while left< right and not title[left].isalpha():
            left +=1
        while left<right and not title[right].isalpha()      :
            right-=1

        if title[left].lower()== title[right].lower():
            left+=1 
            right-=1
        else :
            return False
        
    return True

print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media")) 

'''
You track your daily engagement rates as a list of integers, sorted in non-decreasing order.
 To analyze the impact of certain strategies, you decide to square each engagement rate 
 and then sort the results in non-decreasing order.

Given an integer array engagements sorted in non-decreasing order, return an array of the 
squares of each number sorted in non-decreasing order.
'''

