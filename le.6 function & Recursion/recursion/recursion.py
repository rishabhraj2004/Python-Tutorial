#recuesive function 
def show(n):
    if n == 0:  #if n == 0 and return is base case of rcursion if we not define the base case then the recursion will infinite and it will give us error of maximum recursion depth exceeded or code khud pe khud band ho jayega 
        return
    print(n)
    show(n-1)

show(5)