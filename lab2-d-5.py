def deliteli(n):
    for d in range(2, n + 1):
        if n == 1 :
            break
        if n % d == 0 and n != 1:
            print(d )
            deliteli(n // d)
            break
    
            
n = int(input())
deliteli(n)


