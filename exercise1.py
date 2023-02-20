number=int(input("Enter the number to check prime or not"))
def prime_number(x):
    if x>1:
        for i in range(2,x+1):
            if x%i==0:
                return -1
                break
            else:
                return sum(range(1,x+1))
                break
    else:
        print("Enter number greater then 1")

p=prime_number(number)
print(p)