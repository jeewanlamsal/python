#WAP program to get the largest number from a list.
def getNumbers(n):
    inp=input(f"Enter {n} numbers seprated by space:")
    inp_after_split=inp.split()
    int_after_cast= [float(val) for val in inp_after_split]
    return int_after_cast
def total(inp_lst):
    s=sum(inp_lst)
    return s
def getLargest(inp_lst):
 largest =max(inp_lst)
 return largest

n=int(input("How many numbers do you want to enter?"))
numbers=getNumbers(n)

print(f"The numbers you entered are:{numbers}")
print(f"The total sum is:{total(numbers)}")
print(f"The largest number is:{getLargest(numbers)}")