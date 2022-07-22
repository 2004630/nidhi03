print("***************practice day-6****************")
print("**********single inheritance****************")
class A:                 #parent class or super class
    def f1(self):
        print('A')
class B(A):               #child class  or sub class
    def f2(self):
        print('B')
ob=B()
ob.f1()              # A -> B  
ob.f2()
print("************multilevel inheritance*********")
class A():
    def f1(self):
        print('A')
class B(A):
    def f2(self):
        print('B')
class C(B):
    def f3(self):
        print('C')
obj1=C()
obj1.f1()
obj1.f2()           # A -> B -> C
obj1.f3()
print("*************hierarchical inheritance************")
class A():
    def f1(self):
        print('A')
class B(A):
    def f2(self):
        print('B')
class C(A):
    def f3(self):
        print('C')
e=C()              
e.f1()
e.f3()
print("****************multiple inheritance***********")
class A():
    def f1(self):
        print('A')
class B():
    def f2(self):
        print('B')
class C(A,B):
    def f3(self):
        print('C')
obj2=C()
obj2.f1()
obj2.f2()
obj2.f3()
print('***********hybrid inheritance********')
class A():
    def f1(self):
        print('H')
class B(A):
    def f2(self):
        print('E')
class C(B):
    def f3(self):
        print('L')
class D(B):
    def f4(self):
        print('L')
class E(C,D):
    def f5(self):
        print('O')
obj3=E()
obj3.f1()
obj3.f2()
obj3.f3()
obj3.f4()
obj3.f5()
class intro:
    def __init__(self):
        print("Hi")
    def name(self):
        print("my name is nidhi")
class skill:
    def learn(self):
        print("algo and design")
class result(intro,skill):
    def employee(self):
        print("selected")
class display(result):
    def disp(self):
        print("congrats")
obj=display()
obj.name()
obj.learn()
obj.employee()
obj.disp()
print(issubclass(intro,skill))
print(issubclass(result,skill))
print(issubclass(display,intro))
print(isinstance(obj,(intro,skill,result,display)))
print(isinstance(obj,int))
print("**********use of super keyword***********")
class _sum:
    a=10
    b=5
    def __init__(self):
        print("sum is:")
class display(_sum):
    def res(self):
              print(super().a+super().b)
obj=display()
obj.res()
print("*********use of self and super keyword**********")
class A:
    a=10
    b=20
    def __init__(self,a,b):
        print('a')
    def m1(self):
        print('m1')
class B(A):
    a=4
    b=5
    def __init__(self):
        A.__init__(12,12)
    def m2(self):
        super().m1()
        print(self.a,self.b)
        print(super().a,super().b)
ob=B()
ob.m1()
ob.m2()
