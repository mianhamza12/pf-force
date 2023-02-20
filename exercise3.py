def sort_function():
    total=0
    first_list=[]
    while total<=0:
        try:
            number=int(input("Enter the length of list"))
            for i in range(number):
                try:
                    first_list.append(int(input("Enter the Number")))
                except ValueError:
                    print("Enter postive number only")
                
            first_list.sort()
            print(first_list)
            
            second_number=input("Want to Add Number Answer only yes or No")
            if second_number=='yes':
                first_list.append(int(input("Enter the number")))
                first_list.sort()
                print(first_list)
                break
            else:
                first_list.sort()
                print(first_list)
                break
        except ValueError:
            print("Enter integer only")
            continue
        
sort_function()