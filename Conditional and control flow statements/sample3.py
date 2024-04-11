#given a number if a number is divisible by 3 it should print fizz
#if the number is divisible by 5 it should print buzz
#if the number is divisible by 15 it should print fizzbuzz
def sample(n):
    if n%3==0 and not n%15==0:
        print("fizz")
    if n%5==0 and not n%15==0:
        print("buzz")
    if n%15==0:
        print("fizz buzz")

def sample2(n):
    
    if n%15==0:
        print("fizz buzz")
    elif n%3==0 :
        print("fizz")
    elif n%5==0 :
        print("buzz")

n=int(input("Enter a number: "))
sample2(n)