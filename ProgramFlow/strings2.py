number = input("Please enter a series of numbers, using any separators you like: ")
# The code below extracts numeric values from a string with various separators and converts them to integers
separators = ""

for char in number:
    if not char.isnumeric():
        separators = separators + char

print(separators) # ,;:

values ="".join(char if char not in separators else " " for char in number).split()
print(sum([int(val) for val in values]))