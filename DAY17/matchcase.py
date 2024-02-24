
# Matchcasing example 1 ...

x = int(input("Enter the value of x : "))
match x:
    case 0:
        print("x is zero")

    case 4:
        print("case is 4")
    case _:
        print(x)



 # Matching example 2 ...
        


        y = int(input("Enter the value of y"))

        match  x:
            case 0:
                print("x is 0")

            case 4:
                print("x is 4 ")

            # case _ if x!=90:
            #     print(x, "isnot 90")

            case _ if x!=80:
                print(x , " is not 80" )

            case _:
                print(x)
                
                








