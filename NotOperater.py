a=22
b=17
c=2

print(not(a==b))

print(not(b==c))

a="dog"
b="cat"

if not (a==b):
    print(a,'and',b,"are different")

a=7
b=10

if not ((a==1)==(b==10)):
    print("hi")

a=int(input("enter a number:"))

if not (a % 2==0):
    print("a is an odd number")