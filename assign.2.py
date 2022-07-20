# -*- coding: cp1252 -*-
print("********************ASSIGNMENT-2******************")
print("1.")
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factiorial : "))
print(factorial(n))
print("2.")
c=input("enter any value or string:")
res=c[::-1]
if (res==c) :
             print("it is palindrome")
else:
       print(" not  a palindrome")
print("3.")
num=int(input("enter any number:"))
n1=0
print(n1)
n2=1
print(n2)
for i in range(2,num):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3)
print("4.")
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
       print(num,"is an Armstrong number")
else:
       print(num,"is not an Armstrong number")
print("5.")
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def div(x,y):
    return x/y 
def mul(x,y):
    return x*y
def mod(x,y):
    return x%y 
def exp(x,y):
    return x**y
print("select option:")
print("1.addition")
print("2.subtraction")
print("3.division")
print("4.multiplication")
print("5.modulus")
print("6.exponent")
while True:
    choice=input("enter choice(1,2,3,4,5,6):")
    if choice in (1,2,3,4,5,6):
                  num1=float(input("enter first number:"))
                  num2=float(input("enter second number:"))
    if choice==1:
        print(num1,"+",num2,"=",add(num1,num2))
        break
    elif choice==2:
        print(num1,"-",num2,"=",sub(num1,num2))
        break
    elif choice==3:
        print(num1,"/",num2,"=",div(num1,num2))
        break
    elif choice==4:
        print(num1,"*",num2,"=",mul(num1,num2))
        break
    elif choice==5:
        print(num1,"%",num2,"=",mod(num1,num2))
        break
    elif choice==6:
        print(num1,"**",num2,"=",exp(num1,num2))
        break
    else:
        print("Invalid Input")
print("6.")
print("half left pyramid")
for i in range(4):
    for j in range(4):
        if i<j :
            print(" ")
        else:
            print('*',end=' ')
    print()
print("7.")
Year=int(input("enter year:"))
if((Year % 400 == 0) or   (Year % 100 != 0) and   (Year % 4 == 0)):   
                                                             print("yes")
else:  
    print ("No")
print("8")
if (n==1):
        print("false")
    elif (n==2):
        print("true")
    else:
        for x in range(2,n):
                      if(n % x==0):
                             print("false")
        print("true")
print("9.")
a=float(input("enter a:"))
b=float(input("enter b:"))
c=float(input("enter c:"))
s=(a+b+c)/2
area=s*(s-a)*(s-b)*(s-c)
print(area)
print("10.")
ls=[10,20,30,40,"hello"]
print(ls[::-1])
print("11.")
ls=[]
for i in range(len(ls)):
    i=int(input())
    ls.append(i)
print(ls)
total=0
for x in range(len(ls)):
              total=total+ls[x]
print(total)
print("12.")
ls=[]
for i in range(5):
        i=int(input())
        ls.append(i)
print(ls)
total=0
for x in range(5):
              total=total+ls[x]
print(total)
average=total/5
print(average)
print(max(ls))
print(min(ls))
print("15.")
set1={10,20,30,"hi",50}
print(set1)
set2={1,3,5,7,9,"hello"}
print(set2)
print(set1.issubset(set2))
print(set2.issubset(set1))
print("16.")
d=set1.symmetric_difference(set2)
print(d)
print(set1.difference(set2))
print(“18.”)
t1=((10,10,10,12),(30,45,56,45),(81,80,39,32),(1,2,3,4))
t2=[]
n=4
total=0
for i in t1:
     if type(i)==tuple:
                     if (len(i)>1):
                               for sub in i:
                                   total=total+sub
                               print(total)
                               average=total/len(i)
                               print(average)
                               t2.append(average)
                               print(t2)
                               total=0
print("13.")
def group_dict(l):
    res={}
    for k,v in l:
        res.setdefault(k,[]).append(v)
    return res
colors=[('yellow',1),('blue',2),('yellow',3),('blue',4),('red',1)]
print(colors)
print(group_dict(colors))
print("14.")
def nested_dictionary(l1, l2, l3):
     result = [{x: {y: z}} for (x, y, z) in zip(l1, l2, l3)]
     return result

student_id = ["S001", "S002", "S003", "S004"] 
student_name = ["Adina Park", "Leyton Marsh", "Duncan Boyle", "Saim Richards"] 
student_grade = [85, 98, 89, 92]
print("Original strings:")
print(student_id)
print(student_name)
print(student_grade)
print("\nNested dictionary:")
ch='a'
print(nested_dictionary(student_id, student_name, student_grade))
print("17.")
L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
L = [t for t in L if t]
print(L)
print("19.")
lower, upper, special, digit = 0, 0, 0, 0
password = input("Enter your password")
if (len(password) >= 6):
    for i in password:
        for word in password.split():
            if(word[0].isupper()):
                upper += 1
        if(i.islower()):
            lower += 1
        if(i.isdigit()):
            digit += 1
        if(i == '@' or i == '$' or i == '_' or i == '#' or i=='&'):
            special += 1
else:
    print("Password should be more than 6 characters")
if (lower >= 1 and upper >= 1 and special >= 1 and digit >= 1):
    print("Valid Password")
else:
    print("Invalid Password")
