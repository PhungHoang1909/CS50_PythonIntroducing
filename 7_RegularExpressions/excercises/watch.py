# In a file called watch.py, implement a function called
# parse that expects a str of HTML as input, 
# extracts any YouTube URL that’s the value of a src attribute of an iframe element therein
# and returns its shorter, 
# shareable youtu.be equivalent as a str. 
# Expect that any such URL will be in one of the formats below. 
# Assume that the value of src will be surrounded by double quotes. 
# And assume that the input will contain no more than one such URL. 
# If the input does not contain any such URL at all, return None.

import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches = re.search(r"src=\"https?://(?:www\.)?youtube\.com/embed/([^\"]+)", s)
    if matches:
        video_id = matches.group(1)
        return f"https://youtu.be/{video_id}"
    else:
        return(f"None")


if __name__ == "__main__":
    main()