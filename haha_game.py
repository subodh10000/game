#write a program in python that sums 2 numbers
name = input ("what is your name? ")
print("Welcome, ", name)
print("Today, we gonna play a game.")
choose = input ("Please enter Y or N to continue: ")
if (choose == "Y"):
    print("Lets start the game.")
    first = int (input ("write the name of first number?    "))
    second = int (input ("write the name of second number ?   "))

    sum = first + second 
    print("The sum of these numbers is ", sum)
    if (sum <= 3):
        print("Thats right dumbass")
    else: 
        print("This is not the case")
else:
    print("Ok good night. You dont have to play.")

 
