print("**********PRACTICE QUESTIONS***************")
print("1.find the substrings in a string using for loop:")
string="abcde"
res = [string[i: j] for i in range(len(string))
       for j in range(i + 1, len(string) + 1)]

print(res)
#output:
#['a', 'ab', 'abc', 'abcd', 'abcde', 'b', 'bc', 'bcd', 'bcde', 'c', 'cd', 'cde', 'd', 'de', 'e']
print("2.list the even numbers in range 422 and 622 with including 622:")
count=0
for i in range (422,623):
    if i%2==0:
        print(i)
        count=count+1
print(count)
print("3.print largest index at which e appears in list,if e not in list print none:")
def las_index(L,e):
    if e in L:
        index_last=len(L)-L[::-1].index(e)-1
        print (index_last)
    else:
        print("none")
las_index([1,5,3,5,4],5)
#output:3
print("4.matrix multiplication:")
A = [[5, 4, 3],  
     [2, 4, 6],  
     [4, 7, 9]]    
B = [[3, 2, 4],  
     [4, 3, 6],  
     [2, 7, 5]]   
multiResult = [[0, 0, 0],    
               [0, 0, 0],    
               [0, 0, 0]]  
for m in range(len(A)):    
   for n in range(len(B)):    
          for o in range(len(B)):    
               multiResult[m][n] += A[m][o] * B[o][n] 
print("The multiplication result of matrix A and B is: ")  
for res in multiResult:    
   print(res)
#output:
'''The multiplication result of matrix A and B is:
   [37, 43, 59]
   [34, 58, 62]
   [58, 92, 103]'''
print("5.hollow square pattern:")
for i in range(5):
    for j in range(5):
        if i==0 or i==4 or j==0 or j==4:
            print("*",end='')
        else:
            print(" ",end='')
    print()
#output:
'''*****
   *   *
   *   *
   *   *
   *****'''
print("6.nested dictionary")
student1={"maths":"63","science":"87","english":"67"}
student2={"maths":"84","science":"65","english":"62"}
student3={"maths":"61","science":"45","english":"90"}
student_rec={"student1":student1,"student2":student2,"student3":student3}
print(student_rec)
#output:
'''{'student1': {'maths': '63', 'science': '87', 'english': '67'},
    'student2': {'maths': '84', 'science': '65', 'english': '62'},
    'student3': {'maths': '61', 'science': '45', 'english': '90'}}'''
