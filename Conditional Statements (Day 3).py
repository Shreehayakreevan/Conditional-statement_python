#This program prompts the user to enter a number, converts the input to a integer, and then checks if the number is positive, negative, or zero using if-elif-else statements.
# Take user input
while True :
    a = int(input("Enter the number :"))
 # Check if the number is positive, negative, or zero
    if a > 0:
        print("It is a Positive number.")
    elif a < 0 :
        print("It is a Negative number.")
    else :
        print("Number is Equal to Zero ")
    x = (input("Do you want to continue : "))
    print(x)
    if x == "yes" :
        continue
    else :
        break
