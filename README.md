# Factorial-Using-recursion
Factorial of a Number Using Recursion

This Python program calculates the factorial of a number using a recursive function.

📌 What is Recursion?

Recursion is a programming technique where a function calls itself repeatedly until a stopping condition is met.

In this program, the factorial() function calls itself with smaller values until it reaches 0 or 1.

💻 Program Code
print("Factorial of a number using recursion\n")

n=int(input("Enter a number you want to take factorial of : "))

def factorial(n):

    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

print("Factorial of the number is : ",factorial(n))
🔍 How the Program Works
Takes a number as input from the user.
Defines a recursive function factorial(n).
Checks the base condition:
If n is 0 or 1, returns 1.
Otherwise:
Multiplies n with factorial(n-1).
Function keeps calling itself until the base condition is reached.
Final result is printed.
▶ Example Output
Example 1
Enter a number you want to take factorial of : 5
Factorial of the number is : 120
Example 2
Enter a number you want to take factorial of : 1
Factorial of the number is : 1
🧠 Recursive Flow Example

For 5!

5!=5×4!
4!=4×3!
3!=3×2!
2!=2×1!
1!=1

Final Answer:

5!=120
📖 Formula Used

n!=n×(n−1)!

🧠 Concepts Used
Functions
Recursion
Base Condition
User Input
Conditional Statements
✅ Advantages of Recursion
Cleaner and shorter code
Easy to understand mathematical problems
Useful for tree and graph problems
⚠ Limitations of Recursion
Uses more memory due to function calls
Slower compared to iteration
Large inputs may cause stack overflow
🔁 Iteration vs Recursion
Iteration	Recursion
Uses loops	Uses function calls
Faster	Slightly slower
Less memory usage	More memory usage
Beginner-friendly	Conceptually powerful
