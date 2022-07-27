print("*********TYPES OF ERRORS***************")
print("1.syntax error")
c=input("enter:")
if c is string         #it will generate syntax error
    print("it is a string")
else:
    print("not a string")
print("2.type error")
geek = "Geeks"
num = 4
print(geek + num + geek)    #it will generate type error becoz num can't be added to a string
print("3.zerodivision error")
a=4
a=a/0   #zerodivision error occurs
print(a)
print("4.name error")
def add(x,y):
    c=a+b 
    print(c)
disp_add(4,5)   #name error occurs
print("5.index error")
l1=[2,4,5,6]
print(l1[5]) #index not present
print("6.key error")
dict={
    1:"red",
    2:"blue",
    3:"green",
}
print(dict[4])     #4 key doen't exist
print("7.value error")
print(int("xyz"))  #invalid literal for int
print("8.indentation error")
if (3>5):
print("hello")         #no space included before print
print("9.modulenot found error")
import mymodule
list=[3,5,7,9,11]
print(list[3])
print("10.attribut error")
x=10
print(x.append(6))   #int has no attribute append

