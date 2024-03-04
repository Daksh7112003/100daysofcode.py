letter = "hey my name is  {} and i am from {}"
country= "India "
name="Harry"

print(letter.format(name ,name)) # this .format method is used 
# but this .format is not used widely .....

#so f string is used ..


print(f"Hey my name is {name} and i am from {country}")

#magic of f string .... its newlt introduced ..............



print(f"Hey my name is {{name}} and i am from {{country}}")
#thats how you can retain the f string , this wont print the value of name , this will print the value "{name}" , exactly like this .....




