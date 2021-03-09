
def chkevenodd(a):
    if(a%2==0):
        return True
    else:
        return False

def main():
    i=int(input("enter number"))
    ret=chkevenodd(i)
    if (ret==True):
        print("even number")
    else:
        print("odd number")
        
        
if __name__=="__main__":
    main()