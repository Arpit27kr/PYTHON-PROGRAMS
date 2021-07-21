#program to write in file
f=open("arpit.txt",'a')
f.write("\n want to append these lines in file")
print("done")
f.close()


#program to read file
f=open("arpit.txt",'r')
call=f.read()
print(call)
f.close()
