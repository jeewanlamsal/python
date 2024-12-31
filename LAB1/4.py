#WAP to display prime numbers from 1 to 100
from math import ceil,sqrt

def list_primes(n1,n2):
    for num in range(n1,n2+1):
        flag=0
        for i in range(2,ceil(sqrt(num))):
            if num%i==0:
             flag=1
        if flag==0:
            print(num,end=" ")
            
n1=int(input("First number:"))
n2=int(input("Second number:"))
list_primes(n1,n2)