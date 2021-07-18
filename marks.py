Marks =0
f=open("marks.txt",'r')
data=f.readlines()[1: ]
print(data)
for i in data:
    record=i.rstrip('\n').split(' ')
    Marks+=int(record[2])
print(Marks)
f.close()

