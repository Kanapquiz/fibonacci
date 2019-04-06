def fibonacci(n):
    if n < 2:
        return n
    fibPrev = 1
    fib = 1
    for _ in range(2, n):
        fibPrev, fib = fib, fib + fibPrev
    return fib

if __name__=="__main__":
    number=int(input("Which element of the fibonacci sequence do you want to display? "))
    print(fibonacci(number))
