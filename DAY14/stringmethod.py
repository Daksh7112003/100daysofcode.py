#strings are immutable .... strings cant be change , it means that it will make a new string everytime....





a="hArry"
print(len(a))
print(a.upper())

print(a.lower())



print(a.replace("hArry" , "John")) # this will replace the word from another ....



print(a.count("r"))


print(a.endswith("y"))  # output will  be true..
print(a.endswith("!!!"))  # output will be false...
#basically it checks that your condition is true or not ..



print(a.startswith("hA")) # same like ends and startwith fxn.......
print(a.istitle())