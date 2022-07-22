print("**************pracctice day-6*************")
print("**********Polymorphism in single inheritance********")
class Add():
	def show(self):
		print("addition is:",a+b)
class Multiply(Add):
	def show(self):
		print("multiplication is:,a*b")
obj2 = Multiply()
obj2.show()
print("**********polymorphism in multiple inheritance**************")
class Parent1():
    def show(self):
        print("Inside Parent1")
class Parent2():
    def display(self):
        print("Inside Parent2")
class Child(Parent1, Parent2):
                   def show(self):
                        print("Inside Child")
obj = Child()
obj.show()
obj.display()
print("************polymorphism in multilevel inheritance**********")
class A:
    def show(self):
        print('A')
class B(A):
    def display(self):
        print('B')
class C(B):
    def show(self):
        print('C')
obj=C()
obj.display()
obj.show()
print("***********polymorphism in hierarachical inheritance************")
class A:
    def show(self):
        print('A')
class B(A):
    def display(self):
        print('B')
class C(A):
    def show (self):
        print('C')
obj=C()
obj.show()
print("**********in-built modules**************")
prit("1.operator module")
from operator import *
a, b = 10, 20    
print(mul(a, b))  #prints the product of the values 'a' and 'b'
print(gt(a, b))  #prints True if the value of 'a' is greater than 'b'. Else, False
print(mod(a, b)) #prints the remainder value, when the value of 'a' is divided by 'b'
print(concat("FACE", "TIME"))  #concatenates and prints the given two strings
print("2.decimal module")
from decimal import *
a, b = 10, 3
c = a / b
print(c)
print(Decimal(c)) #prints the complete decimal value of c
print("3.random module")
from random import *
print(randint(10, 20)) #prints a random number between the given range
list1 = [30, 23, 45, 16, 89, 56]
print(choice(list1)) #prints a random element from the given iterator
print(uniform(10, 20)) #prints a random float number between two given values
print("4.string module")
from string import *
print(capwords("fACE prep")) #capitalizes the first letter of each words
print(ascii_letters) #prints all lowercase and uppercase letters
c="Red color is very bright "
print(c.islower()) #prints true if string contains lowercase characters else false
print("5.math module")
from math import *
print(sqrt(16)) #prints the square root of the value 16 in the form of a floating-point value
print(factorial(5)) #prints the factorial of the value 5
print("*********user-defined modules************")
import re          # import re as r
print(re.sqrt(4)) # print(r.sqrt(4))
print(re.sum(3,5))
