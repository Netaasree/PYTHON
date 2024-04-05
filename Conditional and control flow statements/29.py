def fib(a):
    if a<=0:
        print("Incorrect input!")
    elif a==1:
        return 0
    elif a==2:
        return 1
    else:
        return fib(a-1)+fib(a-2)



a=int(input("Enter a number: "))
print(fib(a))
