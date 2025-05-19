string1 = "he's "
string2 = "probably "
string3 = "pining" 
string4 = "for the"
string5 = " fjords"

print(string1 + string2 + string3 + string4 + string5)  # Concatenation

print("he's " "probably " "pining" "for the" " fjords")  # Implicit concatenation

print("Hello " * 5)  # Repetition

print("Hello " * (5 + 4))
print("Hello " * 5 + "4")  # Repetition and concatenation

today = "friday"
print("day" in today)  # True
print ("fri" in today)  # True
print("thur" in today)  # False
print("parrot" in "fjord")  # False