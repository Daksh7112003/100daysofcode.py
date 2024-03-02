def average(a , b):
    print("the average is " , (a+b)/2)



def average(a , b=1):  #int this case to put b value in the printing average is optional , if u do not take the value of b then it will take the value b=1 ...

    print("the average is " , (a+b)/2)
    
def average(a , b):
    print("the average is " , (a+b)/2)


average(1,5)


  


def japan(*numbers):
    sum = 0  # Initialize the sum variable to 0
    for i in numbers:
        sum = sum + i  # Add each number to the sum

        
    return sum / len(numbers)  # Return the average of the sum divided by the number of arguments

c = japan(5, 1)
print(c)