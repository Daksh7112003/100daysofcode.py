def func():
    try:


        l=[1,3,5,6]
        i =int(input("Enter the index: "))
        print(l[i])
        return 1
    

    except:
        print("Some error occurred ")
        return 0
    
    finally:
        print("I am always executed ")\
        # at this point the value of finally keywords came ..... as this work every time ...


       

x= func()
print(x)
