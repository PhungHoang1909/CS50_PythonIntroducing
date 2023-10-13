#Lecture 4 - Libraries

#Custom Library 

import sys

from sayings import goodbye

if len(sys.argv) == 2:
    goodbye(sys.argv[1])