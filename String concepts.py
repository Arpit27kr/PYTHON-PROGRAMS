# %s is used to insert the string which is missing in the para


balltype="cricket"
result="hit"
print("%s ball stuck with my leg which %s me hard" % (balltype,result))

# %d  use in python

runs=45
match = "cheepauk"

print("In %s stadium Rohit score %d runs  \n " % (match,runs))

#inserting string with place holder {}

name="Malhar"
age=23
percentage=55.5
print("\n \n \n my name is {} and my age is {} years".format(name, age))


#use of capitalize function
name="my name is arpit"
print(name.capitalize())
print(name.upper()) #use of upper()
print(name.lower()) #lower() fn
print(name.title()) #title capitalize first word like title
print(name.find("is")) #it finds and return index
print(name.index("is")) #return index
print(name.count("in")) #count(): This method returns the number of occurrences of a substring in given string.
print(name.isalpha()) #check for alphabet
print(name.isdigit()) #check for digit
print(name.islower()) #check for lower character
print(name.isupper()) #check lower characters

