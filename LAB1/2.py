#WAP to input the percentage and display the division

def division(per):
 if(per>=80):
    print("Distinction")
 elif(per>=65):
    print("First Division")
 elif(per>=55):
     print("Second Division")
 elif(per>=40):
     print("Third Division")
 else:
     print("Fail")
    
    
    
percentage=int(input("Enter your obtained percentage: "))
division(percentage)