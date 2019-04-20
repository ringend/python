#Working for conditional statements

def main():
    x, y = 10, 100
    #conditional use if
    if (x < y):
        result = "x is less than y"
    print(result)

    #conditional use if and else
    x, y = 1000, 100
    if (x < y):
        result = "x is less than y"
    else:
        result = "x is greater than y"
    print(result)

    #conditional use if, else and elif
    x, y = 100, 100
    if (x < y):
        result = "x is less than y"
    elif (x == y):
        result = "x is the same as y"
    else:
        result = "x is greater than y"
    print(result)

    #conditional statement
    x, y = 1000,10
    result = "x is less than y" if (x<y) else "x is greater or tha same as y"
    print("conditional statement")
    print(result)


#End Section
if __name__ == "__main__":
    main()
