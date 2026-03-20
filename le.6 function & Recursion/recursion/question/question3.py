# write a recursive function to print all element in a list
def print_list(list, idx):
    if idx == len(list):
        return
    print(list[idx])
    print_list(list, idx+1)

cities = ["Delhi", "Mumbai", "Kolkata", "Chennai", "Bangalore"]
print_list(cities, 0)
