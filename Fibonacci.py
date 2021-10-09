# Fibonacci series
num = int(input())

def fibonacci(n):
    if n <1:
        return 0
    elif n == 1:
        return 1  
    elif n == 2:
        return 1  
    else:
        a = fibonacci(n-1) + fibonacci(n-2)
    return a

#fibonacci(num)
for  n in range(num):
	print(fibonacci(n))


