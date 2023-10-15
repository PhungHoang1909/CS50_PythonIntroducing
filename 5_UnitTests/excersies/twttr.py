def main():
    text = input("Input: ")
    print(shorten(text))

def shorten(text):
    vowels = "ueoaiUEOAI"
    for c in vowels:
        text = text.replace(c, "")
    return text

if __name__ == "__main__":
    main()