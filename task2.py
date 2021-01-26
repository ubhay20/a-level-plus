class User():
    
    def __init__(self,firstname,surname,email,password):
        self.firstname = firstname
        self.suname = surname
        self.email = email
        self.password = password
       
    def say_entdet(self):
        print("Please enter login details, ", self.firstname)
        entusername = input("Email: ")
        entpassword = input("Password: ")

        return(entusername,entpassword)


my_User = User("Ubhay","Ahmed","ubhay20@gmail.com","1234")

loginsuccess = False

while loginsuccess == False:
    
    inputuser,inputpass = my_User.say_entdet()

    lowerpresent = False
    upperpresent = False
    numberpresent = False

    containsAT = False
    correctlength = False

    if inputuser.count("@") != 1:
        print(" ")
        print("Improper email format. Please use \"xxxxxx@xxxxx.xxx\".")
    elif inputuser.count("@") == 1:
        containsAT = True
        
    if len(inputpass) < 6 or len(inputpass) > 12:
        print(" ")
        print("Password length must be between 6 and 12 characters long")
    else:
        correctlength = True

        
    for c in inputpass:
            if c.islower():
                lowerpresent = True
            elif c.isupper():
                upperpresent = True
            elif c.isnumeric():
                numberpresent = True

    if lowerpresent == False or upperpresent == False or numberpresent == False:
        print(" ")
        print("Your password must contain:")
        print("   An uppercase letter,")
        print("   a lowercase letter,")
        print("   a number.")

        print(" ")

    if containsAT == True and correctlength == True and lowerpresent == True and upperpresent == True and numberpresent == True:
        loginsuccess  = True
        print("Details Accepted")


input("End of script, press enter to exit")
        
