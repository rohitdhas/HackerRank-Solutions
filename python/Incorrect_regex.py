# URL to problem - https://www.hackerrank.com/challenges/incorrect-regex/problem?h_r=profile

# ----PROBLEM STATEMENT----

# You are given a string S.
# Your task is to find out whether S is a valid regex or not. 
# Print True if it's valid otherwise print False.
# _____________________________

# ----SAMPLE INPUT----
# > 2
# > .*\+
# > .*+

# ----SAMPLE OUTPUT----
# > True
# > False
# _____________________________

import re

num_of_inputs = int(input())
for _ in range(num_of_inputs):
    regex = input() 
    try:
        re.search(regex, '')
        print(True)
    except:
        print(False)

# _____________________________
# ----EXPLANATION----
# ---> If a REXGEX is invalid then it will throw an error.
#      Then we can use try catch blocks to know if it's throwing an error or not.
#      If thows error it will print False from catch block otherwise it will print True.