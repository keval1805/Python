f = 1
try:
    x = int(input("Enter the number to get factorial: \n"))

    if x < 0:
        raise ValueError("Factorial is not defined for negative numbers.") 
    for i in range(x, 0, -1):
        f = f * i
except ValueError as error:  
    print(error)
except TypeError as error:
    print(error)
else:
    print(f) 

