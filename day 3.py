print("*********************PRACTICE DAY-3********************")
print("data types for storing multiple values in one variable")
print("1.list")
l1=[10,20,30,40,10,37]
l1.append(23)
print(l1)
l1.sort()
print(l1)
print(min(l1))
print(max(l1))
l1.remove(20)
print(l1)
l1.extend(['my','name','is','nidhi'])
print(l1)
l1.insert(4,'hello')
print(l1)
l1.pop(3)
print(l1)
print(l1.count(10))
print(l1[0:5])
print(l1[::-1])
print(len(l1))
m1=[1,2,3,4]
print(l1+m1)
print(l1*3)
print(l1.index('my'))
print("2.tuple")
t1=(10,20,30,40,50)
print(t1)
print(sorted(t1))
print(min(t1))
print(max(t1))
print(t1[0:4])
print(t1[::-1])
print(len(t1))
print(20 in t1)
print(t1[4])
print("3.sets")
set1={10,20,30,40,87}
set1.update("hello")
print(set1)
set1.remove(20)
print(set1)
print(set1.pop())
set2={1,30,5,77,9}
print(set1.issubset(set2))
print(set1.issuperset(set2))
print(set1.isdisjoint(set2))
a=set1|set2
print(a)
b=set1&set2
print(b)
c=set1.difference(set2)
print(c)
d=set1.symmetric_difference(set2)
print(d)
s1=frozenset(set1)
print(s1)
s2=frozenset(set2)
print(s2)
print("4.dictionary")
dict={'yellow':1,'red':3,'white':5,'neon':6}
print(dict.keys())
print(dict.values())
del dict['yellow']
print(dict)
dict1={'yellow':3,'red':9,'violet':2}
dict1.update(dict)
print(dict1)
if 'red' in dict:
    del dict['red']
else:
    print(dict)
print(len(dict))
print("FUNCTIONS:")
def sum():
    print(10+30)
sum()
def disp(a,b,c):
    d=a+b+c
    print(d)
disp(10,20,30)
def disp(a,b,*c):
    print("\n")
disp(10,20,30,40,50)
print(type(c))
def disp(a,b):
    c=a+b
    return c
res=disp(10,30)
print(res)


