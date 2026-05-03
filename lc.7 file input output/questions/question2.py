#from a file containig numbers sepeated by comma, print the count of even numbers.
count = 0
with open("numbers.txt", "w") as f:
    f.write("1,2,3,4,5,6,7,8,9,10,87,98,91,92,10004")

with open("numbers.txt", "r") as f:
    data = f.read()
    print(data)

    numbers = data.split(",")
    for val in numbers:
        if int(val) % 2 == 0:
            count += 1

print("Count of even numbers:", count)