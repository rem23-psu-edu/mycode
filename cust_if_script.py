#!/usr/bin/env python3
"""Bob testing if, elif, else
   if, elif, else - A simple program using conditionals to make a decision."""


message = 'your network experience is '

# wrap connection in a float() to accept decimals as numbers
connection = int(input("What is your connection speed in Mbps?"))

# if input value was higher or equal to 25
if connection >= 25:
    message = message + 'good'
elif connection >= 5:
    message = message + 'borderline unusable'
elif connection >= 2:
    message = message + 'unusable'
else:
    message = message + 'non-existent'
print(message)

