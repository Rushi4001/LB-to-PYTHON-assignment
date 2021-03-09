
def divisible(a):
    if (a%5==0):
        return True
    else:
        return False

def main():
    x=int(input("enter the number"))
    
    ret=divisible(x)
    if (ret==True):
        print("number is divisible by 5")
    else:
        print("number is not divisible by 5")


if __name__=="__main__":
    main()