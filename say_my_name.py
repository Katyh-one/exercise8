# Assigning string value Katy to variable named firstname
firstname = 'Katy'
# Assigning string value Hatch to variable named firstname
lastname = 'Hatch'
# printing two variables together and will be seperated by a space due to the ,
print(firstname, lastname)

# Assigning the value of variables firstname plus a space plus a lastname to the new variable named fullname
fullname = firstname + ' ' + lastname
# printing the variable fullname
print(fullname)
# checking the type of value fullname is
print(type(fullname))

def sayMyName():
    print ("My name is " + fullname + ".")

sayMyName()