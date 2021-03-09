def display(a):
    for i in range (0,a):
        print("*",end="")

def main():
    i=int(input("accept number from user to print *"))
    display(i)

if __name__=="__main__":
    main()