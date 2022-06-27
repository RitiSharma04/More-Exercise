from ast import Pass


password =input("enter the password:-")
if len(password)<=12 and len(password)>=8:
    if password>"a"and password>"z"or password>"A" or password<"Z":
        if "@" in password or "#" in password or "$" in password:
            if password>"1" or password<"9":
                print("yes")
            else:
                print("no")
        else:
            print("no")
    else:
        print("no")                    
else:
    print("no")                