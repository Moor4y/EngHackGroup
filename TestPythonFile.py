#Data Storing 
arrQ = ["What is your learning style?",    #array to store question information
        "Would you like to work in the natural environment?",
        "Like studying rocks and dirt?",
        "Would you like to work with buildings and infrastructure?",
        "Do you prefer artistic design or structural planning?",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        ""]

arrA = ["Gimme the hands on stuff",   #array to store option A information
        "I love working with nature.",
        "I'm mining for diamonds",
        "I love buildings.",
        "artistic design",
        "",
        "",
        "",
        "",
        "",
        ""]
arrB = ["Gimme the hands off stuff",  #array to store option B information
        "I would rather not work with nature.",
        "No, that sounds boring.",
        "I hate buildings.",
        "structural planning",
        "",
        "",
        "",
        "",
        "",
        ""]
arrComment = ["",                                       #array to store comment information
              "",
              "",
              "",
              "",
              "",
              "",
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

#branch 1
if userInput == 'A': #hands on
    printQuestion(arrQ[1],arrA[1],arrB[1])
    userInput = getMCPick()
    if userInput == 'A': #love nature
        printQuestion(arrQ[2],arrA[2],arrB[2])
        userInput = getMCPick()
        if userInput == 'A': #love rocks:
            print ("You belong in Geological Engineering.")
        else: #no rocks
            print ("You belong in Environmental Engineering.")
    else: #no like nature
        printQuestion (arrQ[3], arrA[3],arrB[3])
        userInput = getMCPick()
        if userInput == 'A': #love buildings
            printQuestion (arrQ[4], arrA[4],arrB[4])
            userInput = getMCPick()
            if userInput == 'A':
                print ("You belong in Archetectural Engineering")
            else:
                print ("You belong in Civil Engineering")


            


