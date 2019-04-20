from math import sqrt
import time
def isPrime(n):
    count=2
    res=[]
    a=sqrt(n)
    while(count<=a):
        if n%count==0:
            res.append(count)
            n=n/count
        else:
            count+=1
            continue
    if n!=1:
        res.append(int(n))
    return res
number=eval(input("input the number:"))
start=time.perf_counter()
print(isPrime(number))
elapsed=time.perf_counter()-start
print(elapsed)
