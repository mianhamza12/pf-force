def student():
    total_student=int(input("Enter Total Number in the class"))
    if total_student>=0:
        math_student=int(input("Enter Number of students with mathematics in the Class"))
        bio_student=int(input("Enter Number of students with Bio in the class"))
        if math_student >= total_student or bio_student >= total_student:
            print("value not correct")
        else:
            total=total_student-(math_student+bio_student)
            print("Total sutdent without Bio & math is :",total)
            print("Total number with Bio & Math is :",total_student)    
    else:
        print("Enter Correct Value")
        
student()
    

