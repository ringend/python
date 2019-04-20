
# Varibles Section
f=0
print(f)

f="abc"
print(f)

print ("123 "+ "456")

#Functions
def somefunct():
    f="Functions"
    print(f)

somefunct()
print(f)


#Global Varibles
def somefunct():
    global f
    f="Global Vars"
    print(f)

somefunct()
print(f)
