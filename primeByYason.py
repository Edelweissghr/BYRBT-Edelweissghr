#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# _author_ = ' Yasen '
#==========================
from math import floor
import time


res = []

def fact(number,k):
    if(number == k):
        res.append(k)
        return
    while(number%k==0):
        number = number/k
        res.append(k)
    if(number == 1):
        return
    else:
        k += 1
        fact(number,k)

def main():


    number = eval(input("Input your number:"))
    starttime = time.perf_counter()
    #res = getPrime(number)
    fact(number,2)
    print("{}".format(res))
    endtime = time.perf_counter() - starttime
    print(endtime)


#==========================
if __name__ == '__main__':
    main()