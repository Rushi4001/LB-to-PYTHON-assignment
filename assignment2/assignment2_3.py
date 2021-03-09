
def compare(a):
    if(a<10):
        return True
    else:
        return False

def main():
    i=int(input("enter number"))
    ret=compare(i)
    if (ret==True):
        print("hello")
    else:
        print("demo")
        
        
if __name__=="__main__":
    main()