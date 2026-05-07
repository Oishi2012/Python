file1=open("f1.txt","r")
file2=open("f2.txt","w")

for line in file1.readlines():
    if not(line.startswith('Coding')):
        print(line)
        file2.write(line)

file1.close()
file2.close()

count=0
for line in open("f1.txt","r").readlines():
    if not(line.startswith('Coding')):
        print(line)
        file2.write(line)
        count=count+1
print("Total lines copied:",count)
file1.close()
file2.close()