def fib():
    print('This program will print all Fibonacci numbers up to your input on one line.')
    print('Please type a positive integer.')
    n = input()
    try:
        n = int(n)
    except ValueError:
        print("You must input an integer.")
        return
    n = int(n)
    ntype = type(n)
    if ntype != int:
        print('You must input an integer.')

    else:
        if n < 1:
            print('You must insert a value greater than 0.')
        else:
            a, b = 0, 1
            while a < n:
                print(a, end=' ')
                a, b = b, a+b
        print()
    start()

def fib2():
    print('This program will create a stack of all Fibonacci numbers up to your input on one line.')
    print('Please type a positive integer.')
    n = input()
    try:
        n = int(n)
    except ValueError:
        print("You must input an integer.")
        return
    n = int(n)
    ntype = type(n)
    if ntype != int:
        print('You must input an integer.')

    else:
        if n < 1:
            print('You must insert a value greater than 0.')
            return
        else:
            result = []
            a, b = 0, 1
            while a < n:
                result.append(a)
                a, b = b, a+b
        print(result)
    start()

def fiblist():
    #get input; check if it's an integer
    print('This program will export a list of the first (n) Fibonacci numbers')
    print('in a sequence, where (n) is based on your input.')
    print('Please type a number. ')
    n = input()
    try:
        n = int(n)
    except ValueError:
        print("You must input an integer.")
        return
    n = int(n)
    ntype = type(n)
    if ntype != int:
        print('You must input an integer.')

    else:
        if n < 1:
            print('You must insert a value greater than 0.')
        else:
            a, b = 0, 1
            for i in range(n):
                print(i+1,'\t-\t', f'{a:,}')
                a, b = b, a+b
    start()

def fibfind():
    #get input; check if integer
    print('Please type a number. ')
    n = input()
    try:
        n = int(n)
    except ValueError:
        print("You must input an integer.")
        return
    n = int(n)
    ntype = type(n)
    if ntype != int:
        print('You must input an integer.')

    else:
        if n < 1:
            print('You must insert a value greater than 0.')
        else:
            a, b = 0, 1
            for i in range(n):
                if i < n:
                    f = a
                    a, b = b, a+b
            print(n, '\t-\t', f'{f:,}')
    start()

def start():
    print('Please select an option:\n1) fib()\n2) fib2()\n3) fiblist()\n4) fibfind()\n0) Exit to shell')
    choice = input()
    if choice == '1':
        fib()
    elif choice == '2':
        fib2()
    elif choice == '3':
        fiblist()
    elif choice == '4':
        fibfind()
    elif choice == '0':
        print('Type "start()" to run the module again.')
    else:
        print('Invalid choice.')
        start()

start()
