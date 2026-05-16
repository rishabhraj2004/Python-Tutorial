#eg of multiple inheritence 
#ismai multiple class ke properties ko ek hi drive class mai use kar saktey hai.
class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class b"

class C(A, B):
    varC = "welcome to class C"

c1 = C()

print(c1.varC)
print(c1.varA)
print(c1.varB)