#WAP to check if an input number is odd or even

def odd_even(num):
    if(num%2==0):
        print("Even Number")
    else:
        print("Odd Number")
        
value=int(input("Enter a number:"))
odd_even(value)