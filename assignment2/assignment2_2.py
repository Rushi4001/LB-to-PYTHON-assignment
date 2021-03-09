
def display(a):
    while(a>0):
        print("*")
        a=a-1

def main():
    i=int(input("accept number from user to print *"))
    display(i)

if __name__=="__main__":
    main()