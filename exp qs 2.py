sumofarea=0
f=open("city.txt",'r')
city_name=[]
city_details=f.readlines()
print(city_details)
for i in city_details:
    data=i.rstrip('\n').split()
    print(data)
if float(data[1])>10:
        city_name.append(data[0])
print("city with population more than 10 lakh:-",city_name)    


for i in city_details:
    data= i.rstrip('\n').split()
    sumofarea+= int(data[2])
print("total area of city",sumofarea)

