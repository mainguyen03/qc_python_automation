
n = int(input("Enter the number of rows: "))  

def halfPyramid():
    k = 2 * n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 2
        for j in range(0, i + 1):
            print("*", end=" ")
        print("\r")

def halfPyramid_reverse():
    k = 2 * n - 2
    for i in range(0, n):
        if i == (n -1):
            print ("* " * 2 * n, end="")
            pass
        else: 
            for j in range(0, k):
                print(end=" ")
            k = k - 2
            for j in range(0, i + 1):
                print("*", end=" ")
            print("\r")
    k = n 
    print("\r")
    for i in range(n, -1, -1):
        for j in range(k , 2*n):
            print(end=" "*2)       
        for j in range(1, i ):
            print("*", end=" ")
        print(" ")

while True:
    print("1. Print Half Pyramid of Stars")
    print("2. Print Reverse Half Pyramid of Stars")
    print("3. Exit")
    print("Enter Your Choice: ", end="")
    choice = int(input())
    if choice==1:
        halfPyramid()
    elif choice==2:
        halfPyramid_reverse()
    elif choice==3:
        print("Exiting...")
        break
    else:
        print("Wrong Choice!")


