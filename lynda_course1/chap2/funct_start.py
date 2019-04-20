
#Define a Function
def funct1():
    print("I am funct1")

#functions with arguments
def funct2( arg1, arg2):
    print(arg1, " ", arg2)

#fuction that return a value
def cube(x):
    return x*x*x

#fuction with default valude for an arg
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

#fuction with vaiable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

#Results Section
funct1()
print(funct1())

print("Start funct2 section")
funct2(10,20)
print(funct2(10, 20))
print(cube(3))

print("Start power section")
print(power(2))
print(power(2,3))
print(power(x=3, num=2))

print("Multi Add Function")
print(multi_add(1,2,3))
print(multi_add(10, 1,2,3))
