print("**************************ASSIGNMENT-1******************")
print("1.")
name='my first python class'
print(len(name))
print("2.")
fname='mississippi'
print(fname.count('s'))
print("3.")
m=input('enter:')
print(m)
if len(m)<2:
        print('empty string')
else:
     print(m[0:2]+m[-2:])
print("4.")
c=input('string')
temp=c[0]
for i in range(1,len(c)):
               if(c[0] == c[i] ):
                      temp = temp + '$'
               else:
                  temp = temp + c[i]
print(temp)
print("5.")
p=input('string')
q=input('string')
new_p = q[:2] + p[2:]
new_q = p[:2] + q[2:]
print(new_p + ' '+new_q)
print("6.")
c=input('string')
if len(c)>=3:
    if c[-3:]=='ing':
                   c=c+'ly'
                   print(c)
    else:
        c=c+'ing'
        print(c)
else:
    print('less than 3')
print("7.")
str1=input("enter a string:")
snot=str1.find('not')
spoor=str1.find('poor')
if spoor>snot and snot>0 and spoor>0:
         str1=str1.replace(str1[snot:(spoor+4)],'good')
         print(str1)
else:
   print(str1)
print("8.")
def  longest(a):
    max1=len(a[0])
    temp=a[0]
    for i in a:
        if len(i)>max1:
            max1=len(i)
            temp=i
    print("the longest word is:",temp,"and length is:",max1)
l1=["red","exercise","blue","white"]
longest(l1)
print("9.")
c=input('string')
index=int(input())
changed_string=''
for char in range(0,len(c)):
                    if char!=index :
                    changed_string+=c[char]
print(changed_string)
print("10.")
c=input('string')
new_string=c[-1]+c[1:-1]+c[0]
print(new_string)
print("11.")
c=input('string')
new_string=''
for char in range(len(c)):
                     if char%2==0:
                     new_string+=c[char]
print(new_string)
print("12.")
c=input("enter a sentence") 
char=input('char')
counter=c.count(char)
print(counter)
print("13")
c=input('string')
print(c.lower())
print(c.upper())
print("14.")
c=input('string')
print(c.lower())
print(c.upper())
print("15.")
def add_tags(tag, word):
	return "<%s>%s</%s>" % (tag, word, tag)
print(add_tags('i', 'Python'))
print(add_tags('b', 'Python Tutorial'))
print("16.")
def insert_sting_middle(str, word):
	return str[:2] + word + str[2:]
print(insert_sting_middle('[[]]', 'Python'))
print(insert_sting_middle('{{}}', 'PHP'))
print(insert_sting_middle('<<>>', 'HTML'))
print("17.")
def insert_end(str):
	sub_str = str[-2:]
	return sub_str * 4
print(insert_end('Python'))
print(insert_end('Exercises'))
print("18.")
def made_string(str):
             if len(str)>=3:
                       return str[:3]
             else:
                print(str)
print(made_string('ipy'))
print(made_string('python'))
print(made_string('hello'))
print("19.")
str1='https://www.w3resource.com/python-exercises/string'
print(str1.rsplit('/',1)[0])
print(str1.rsplit('-',1)[0])
print("20.")
def rev_string(str):
          if len(str)%4==0:
               return str[::-1]
          return str
print(rev_string('python'))
print(rev_string('swap'))
print("21.")
def to_uppercase(str1):
    num_upper = 0
    for letter in str1[:4]: 
        if letter.upper() == letter:
            num_upper += 1
    if num_upper >= 2:
        return str1.upper()
    return str1

print(to_uppercase('Python'))
print(to_uppercase('PyThon'))
print("22.")
str1 = "\n Starbucks has the best coffee \n"
newstr = str1.strip()
print(newstr)
print("23.")
text = "Python is easy to learn."
result = text.startswith('is easy')
print(result)
result = text.startswith('Python is ')
print(result)
result = text.startswith('Python is easy to learn.')
print(result)
