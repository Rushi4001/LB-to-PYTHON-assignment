
def divnum(a,b):
    c=a/b
    return c


def main():
    print("enter first number")
    x=int(input())
    print("enter second number")
    y=int(input())
    
    iret=divnum(x,y)
    print("division of number is {}".format(iret))



if __name__=="__main__":
    main()