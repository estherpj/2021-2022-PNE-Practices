def fib(n):
    n1 = 0
    n2 = 1
    if n == 1:
        return n1
    elif n == 2:
        return n2
    else:
        for i in range(2, n + 1):
            num = n1 + n2
            n1 = n2
            n2 = num
        return num #you must put the return function outside the loop, if not its going to print the number


print("5th Fibonacci's term:",fib(5))
print("11th Fibonacci's term:",fib(11))
print("55th Fibonacci's term:",fib(55))