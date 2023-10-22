"""
Lecuter 9 - Et Cetera
Map
"""

def main():
    yell("This", "is", "order!")

def yell(*words):
    uppercased = map(str.upper, words)
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)

if __name__ == "__main__":
    main()