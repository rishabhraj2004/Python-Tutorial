#WAF to print the element of a list in a single line.
cities = ["New York", "London", "Paris", "Tokyo"]
heroes = ["Superman", "Batman", "Wonder", "thor"]
def print_list(list):
    for item in list:
        print(item, end=" ") #end=" " is used to print the elements in a single line with space

print_list(cities)
print()  # Print a newline or seperate hero and cities list
print_list(heroes)