# Working with Files

def main():
    #Open a file for writing and create it is needed
    # "w+"" means create new file or overwrite existing file
    #f = open("textfile.txt","w+")

    #Append to existing File
    # "a" means append to existing file
    #f = open("textfile.txt","a")

    #Open a file for reading
    # "r" means open for reading
    f = open("textfile.txt","r")

    #Read the whole File
    #if f.mode =='r':
    #    contents = f.read()
    #    print(contents)

    #Read a file line at a time
    if f.mode =='r':
        fl = f.readlines()
        for x in fl:
            print(x)

    #write to a Files
    #for i in range(10):
    #    f.write("This is a line" + str(i) +"\r\n")


    #close the file when done
    #f.close()

#End Section
if __name__ == "__main__":
    main()
