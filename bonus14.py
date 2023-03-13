from converters14 import convert
from parsers14 import parse

feet_inches = input("Enter feet and inches: ")

parsed = parse(feet_inches)

result = convert(parsed['feet'], parsed['inches'])

print(f" {parsed['feet']} feet and {parsed['inches']} inches is equal to {result} meters")

if result < 1:
    print("Kid can't use the Slide")
else:
    print("Kid can use the Slide")