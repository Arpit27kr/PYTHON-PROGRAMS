#program to append the text in file

file=open("arpit.txt",'a')
file.write("this is my program test \n for append the text in a file ")
print("written  perfectly")
file=open("arpit.txt",'r')
call=file.read()
print(call)
file.close()
