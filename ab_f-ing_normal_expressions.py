
import re

with open(r"C:\Users\craig\OneDrive\Documents\Coding Temple\Workshops\Week_03\W3_Day1\Homework\regex_test.txt") as file:
    data = file.readlines()

print(data)

for person in data:
    test = re.match(r'([A-Z][a-z]+ )', person)
    if test == None:
        print(None)
    elif test:
        test = re.match(r'([A-Z][a-z]+ )([A-Za-z] )([A-Z][a-z]+)$', person)
        print(person)


