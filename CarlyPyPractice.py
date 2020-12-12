#what's your score
scoreInt= int(input("What score did you receive?"))
#tell you your letter grade
if scoreInt >= 90:
    print("Your letter grade is an A")
elif scoreInt >= 80:
    print("Your letter grade is a B")
elif scoreInt >= 70:
    print ("Your letter grade is a C")
elif scoreInt >= 60:
    print("Your letter grade is a D")
else:
    print(" You flunked")

