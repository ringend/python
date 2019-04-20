# Working with Loops

def main():
    x=0

    #deine a while Loop
    print("while loop example")
    while (x<5):
        print(x)
        x=x+1

    #define a for Loop
    print("For loop example")
    for x in range(1, 5):
        print(x)

    #using for on objects
    print("For with objects")
    days=("Mon", "Tues", "Wed")
    for d in days:
        print(d)

    #using break and contine statements
    print("Using break")
    for x in range(5,10):
        if (x==7): break
        print(x)

    print("Using contine")
    for x in range(5,10):
        if (x % 2 == 0): continue
        print(x)

    #using enumerate() fuction to get index
    print("enumberate for index")
    days=("Mon", "Tues", "Wed")
    for i,d in enumerate(days):
        print(i, d)

#End Section
if __name__ == "__main__":
    main()
