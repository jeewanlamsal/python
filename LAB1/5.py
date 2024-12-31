#WAP to enter the marks of 10 students and display it.
num=int(input("Enter the number of subjects: "))
sub=[]
def subject(num):
 for i in range(1,num+1):
     n=int(input("Enter the marks of subject"))
     sub.append(n)
 return sub
     
print(subject(num))