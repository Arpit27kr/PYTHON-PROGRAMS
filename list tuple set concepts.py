#set
S1=set("Internshala")
print(S1)
S2=set([45,67,87,36,55])
print(S2)
S3=set((10,25,15))
print(S3)

#copy command in set

S1=set({"Python", "Java", "C++"})
print(S1)
S1.add("Perl")
print(S1)

a=4
b=a
a="internshala"
print(b)

var="arpit"
print(var.index(P))



capacity=20000
cost=3400

n=int(input("Enter the capacity of power bank"))
c=int(input("Enter the cost of powerbank"))

if n>10000 & c< 3500:
    print("'Yes, this power bank is for you!' if both the requirements are met")
else:
    print("No, this doesn't suit your needs.' if either condition is not met.")

