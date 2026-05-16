print("Factorial of a number using recursion\n")
n=int(input("Enter a number you want to take factorial of : "))
def factorial(n):
    
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

print("Factorial of the number is : ",factorial(n))    