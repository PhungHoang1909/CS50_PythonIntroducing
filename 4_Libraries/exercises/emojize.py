# In a file called emojize.py, implement a program that prompts the user for a str 
# in English and then outputs the “emojized” version of that str, 
# converting any codes (or aliases) therein to their corresponding emoji.

import emoji 

str = input("Input: ")
str = emoji.emojize(str, language='en')
print("Output:", str)