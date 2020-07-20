def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

def fiblist(n):
    a, b = 0, 1
    for i in range(n):
        print(i+1,'\t-\t',a)
        a, b = b, a+b
