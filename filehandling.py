f=open('test.txt','r+')
f.write("good morning")           
f.writelines(["\n hi ,my name is nidhi"])
print(f.read())
content=f.readline()
print(content)
f.close()