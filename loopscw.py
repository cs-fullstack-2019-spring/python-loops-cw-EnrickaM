def main():
    #problem1()
    #problem2()
    #problem3()
    problem4()

# Print -20 to and including 50. Use any loop you want.
#def problem1():
   #numbers=[-20,50]
   #for x in numbers:
    #print(x)

#Create a loop that prints even numbers from 0 to and including 20.

#def problem2():
    #numbers=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    #for x in range (0,20,2):
       # print(x)

#Prompt the user for 3 numbers.
# Then print the 3 numbers along with their average after the 3rd number is entered.
#def problem3():
   # num1=int(input("Enter a number."))
    #num2= int(input("Enter another number."))
   # num3= int(input("Enter your last number "))
    #average= int(str(num1 + num2 + num3))
    #print("The average of " +(str(average)))


#Password Checker -
# Ask the user to enter a password.
# Ask them to confirm the password.
# If it's not equal, keep asking until it's correct or they enter 'Q' to quit.

def problem4():
    while True:
        password=(input("Enter a password."))
        password2 = (input("Enter your password again."))
        if(password=="q"):
            break
        if(password==password2):
            print("Correct")
            break
        else:
            print("THAT'S NOT CORRECT")

























if __name__ == '__main__':
        main()
