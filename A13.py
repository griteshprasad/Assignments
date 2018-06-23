##1.Write a Python program to read  lines of a file.

f = open("Gritesh.txt","w")
f.write("This file is the copy right to all \nthe programs in the current folder.")

f = open("Gritesh.txt","r")
print(f.read())


##2.Write a Python program to copy the contents of a file to another file

a = open("Gritesh.txt","r")
content = a.read()
b = open("Prasad.txt","w")
b.write(content)
b = open("Prasad.txt","r")
print("\n\n",b.read())


##3.Write a Python program to combine each line from first file with the corresponding line in second file.

print()
with open("Gritesh.txt","r") as x:
    with open("Prasad.txt","r") as y:
        for line1,line2 in zip(x.readlines(),y.readlines()):
            print(line1,line2)

x.close()
y.close()
        
		
