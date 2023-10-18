#Lecture 7 - Regular Expressions

import re 

url = input("URL: ").strip()

# re.sub(pattern, repl, string, count = 0, flags = 0)

# username = re.sub(r"(^https?://)?(www\.)?twitter\.com/", "", url)
# print(f"username: {username}")

matches = re.search(r"^https?://(www\.)?twitter.com\.com/(.+)$", url, re.IGNORECASE)

if matches:
    print(f"username:", matches.group(2))