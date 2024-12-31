#WAP to calculate sum, diff, product and quotient between two input numbers using a single function.
def calculate(num1,num2):
    sum=num1+num2
    diff=num1-num2
    product=num1*num2
    quotient=num1/num2
    return sum, diff, product, quotient
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
tup=calculate(a,b)
print("Sum=",tup[0])
print("Diff=",tup[1])
print("Product=",tup[2])
print("Quotient=",tup[3])