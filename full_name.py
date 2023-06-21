full_name = input("Please enter your full name: ")

if len(full_name) < 0:
    print("You haven't entered anything, please enter your full name.")
elif len(full_name) < 4:
    print("You have entered fewer than 4 characters. Please make sure you have entered your full name.")
elif len(full_name) > 25:
    print("You have entered over 25 characters. Please make sure you have only entered your full name.")
else: 
    print("Thank you for entering your name!")

    #nice and simple