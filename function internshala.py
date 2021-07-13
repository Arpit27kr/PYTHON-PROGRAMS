###functions 
##def varchar(m1,m2,m3):
##    total=m1+m2+m3
##    if total>1500:
##        print("you can buy")
##    else:
##        print("you can not  buy")
##    return
##m1=int(input("total savings from gifts"))
##m2=int(input("total savings from pocket money"))
##m3=int(input("total saving from internship"))
##varchar(m1,m2,m3)


##def myfunc(n):
##  return lambda a : a * n
##
##mydoubler = myfunc(2)
##
##print(mydoubler(11))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
