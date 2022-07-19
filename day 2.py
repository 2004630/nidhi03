print("******************PRACTICE DAY-2*********************")
print("operators")
print("1.arithmetic operator")
print(10/2)
print(4+5)
print(10//2)
print(2**3)
print(5%2)
print("2.relational operator")
print(5<6)
print(115>44)
print(15>=15)
print(115<=15)
print(15==15)
print(15!=20)
print("3.logical operator")
print(15>4 and 20<3)
print(20>40 or 20>4)
print(not(15>4))
print("3.assignmet operator")
a=15
b=20
print(a==b)
a=a+4
print(a)
print("4.bitwise operator")
print(10&5)
print(4|5)
print(~4)
print(10<<2)
print(10>>2)
print("5.identity operator")
c=15
d=20
print(c is d)
print(c is not d)
print("6.membership operator")
ab="python class"
print('t' in ab)
print('z'not in ab)
print("control statements")
print("1.conditional statements")
ab="my python class"
print("if statement")
if 't' in ab:
    print("yes")
print("if-else statement")
if 't' not in ab:
    print("yes")
else:
    print("no")
print("nested if-else statement")
a=10
b=5
c=8
if(a<b and c<b):
    print("b is larger than a and c")
elif (a>b and a>c):
        print("a is greater than b and c")
else:
    print("c is greater than a and b")
print("2.looping statements")
print("for statement")
for x in range(10):
    print(x)
print("nested for statement")
for x in range(4):
    for y in range(4):
        print(x,y)
print("3.jumping statement")
print("break statement")
for i in range(10):
    if i==5:
        break
    else:
        print(i)
print("continue statement")
for i in range(10):
    if i==5:
        continue
    else:
        print(i)
print("pass statement")
for i in range(10):
    if i==5:
        pass
    else:
        print(i)
