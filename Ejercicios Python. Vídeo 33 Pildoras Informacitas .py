
User_email = input("Introduce your email: ")

at = User_email.count("@")

if (at !=1 or  User_email.rfind("@")==(len(User_email)-1 or User_email.find("@")==0)):
    print(f"Email incorrect")

else:
    print(f"Email is correct")



