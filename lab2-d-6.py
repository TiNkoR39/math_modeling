


def deliteli(a):
    global count
    global i
    if a > 1 or count > 0:
                 
        for d in range(1, a):
            
            if a % d == 0 and a != 1:
                count = count + d 
               
                
        if count == i:
            print (i)
    
            
n = int(input())
for i in range(1,n+1):
    count = 0
    deliteli(i)
    
