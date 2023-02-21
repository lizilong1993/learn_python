import re

string = "The rain in Spain"
x = re.search("^The.*Spain$", string)

if x:
    print("YES! We have a match!")
else:
    print("No match")
