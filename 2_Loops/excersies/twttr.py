# In a file called twttr.py, implement a program that prompts the user for a str of text 
# and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, 
# whether inputted in uppercase or lowercase.

def main():
    text = input("Input: ")
    print("Output:", text_output(text))

def text_output(text):
    vowels = "ueoaiUEOAI"
    for c in vowels:
        text = text.replace(c, "")
    return text

main()