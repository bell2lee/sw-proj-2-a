def factorial(n):
    if n <= 1:
        return n
    else:
        return n * factorial(n - 1)

if __name__ == "__main__":
    while True:
        comm = int(input("Enter a number: "))
        if comm == -1:
            break
        print("%s! = %d" %(comm, factorial(comm)))