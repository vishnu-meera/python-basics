correct_pass = "Meera@ae0624"
name = "Vishnu"
while True:
    password = input("Enter your password");
    if(password==correct_pass):
        print("hi %s %s you are logged in." % (name,"Sankar"))
        break
    print("Wrong pass, enter it again")
