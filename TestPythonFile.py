#Data Storing 
arrQ = ["Do you like hands on work or programming?",    #array to store question information
                 "",
                 ""]
arrA = ["Hate programming, gimme the hands on stuff",   #array to store option A information
          "",
          ""]
arrB = ["Programming master race",                      #array to store option B information
          "",
          ""]
arrComment = ["",                                       #array to store comment information
              "",
              ""]

#procedures
def printQuestion(Q,A,B):        #procedure to print the question
    print(Q)                     #prints question
    print("Option A:", A)        #prints option A
    print("Option B:", B)        #prints option B
    
def getMCPick():                 #procedure to track user selection
    while True:                  #runs while the user enters A or B in lowercase or uppercase
        choice = input("Please enter either A or B: ")
        if choice == 'A' or choice == 'a':      #checks if the user selects option A
            choice = 'A'                        #standardizes user choice 
            break                               #exits while loop
        elif choice == 'B' or choice == 'b':    #checks if the user selects option B
            choice = "B"                        #standardizes user choice 
            break                               #exits while loop
        else:
            print ("Please only enter A or B")  #prints error prompt
    return choice                               #returns standardized choice

#obtain user info
userName = str(input("Please enter your name: "))                    #asks for user name
print ("Welcome,", userName, "to the Engineering Program selector.") #prints name in a welcome message

#error checking student Grade
while True:
    try:
        userGrade = int(input("Please enter your Grade as a number.\n"
        + "If you are in university, please enter 0: "))
        break
    except: 
        print ("Please enter a number.")
if userGrade <= 12 and userGrade >= 1:
    print ("Great job of researching your post-secondary options!")
elif userGrade == 0:
    print ("Why are you doing this quiz if you already have a major? Get a life!")

printQuestion(arrQ[0],arrA[0],arrB[0])
userInput = getMCPick()
