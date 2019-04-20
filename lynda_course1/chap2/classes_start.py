# Working with Classes

class myclass():
    def method1(self):
        print("myclass method1")

    def method2(self, somestring):
        print("myclass method2 " + somestring)

class myclass2():
    def method1(self):
        myclass.method1(self)
        print("myclass2 method1")

    def method2(self, somestring):
        print("myclass2 method2 ")


def main():
    c = myclass()
    c.method1()
    c.method2("This is a string")

    c2 = myclass2()
    c2.method1()
    c2.method2("This is a string")

#End Section
if __name__ == "__main__":
    main()
