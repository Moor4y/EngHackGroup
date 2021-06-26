#Data Storing 
arrQ = ["What is your learning style?",    #array to store question information
        "would you like to work in the natural environment",
        "Like studying rocks and dirt?",
        "Would you like to work with buildings and infrastructure",
        "Do you prefer artistic design or structural planning?",
        "Would you like to work in a lab or [blank]?",
        "How about medicine?",
        "Would you prefer working in research and development or keeping your options open?",
        "Are you interested in creating moving parts that work together?",
        "Like robots?",
        "Would you like to focus on hardware and technology or do you have a wider range of engineering interests?",
        "Would you like to work with computer parts or with power and energy?",
        "Medicine?",
        "",
        "",
        "",
        ""]

arrA = ["Gimme the hands on stuff",   #array to store option A information
        "I love working with nature.",
        "I'm mining for diamonds",
        "I love buildings.",
        "artistic design",
        "Gimme my lab coat.",
        "Yes, medicine is bae.",
        "Let's keep it broad",
        "I want to make machines.",
        "Robots are my jam.",
        "Hardware and Tech please",
        "Power and Energy",
        "Nah bro",
        "",
        "",
        "",
        ""]
arrB = ["Gimme the hands off stuff",  #array to store option B information
        "I would rather not work with nature.",
        "No, that sounds boring.",
        "I hate buildings.",
        "structural planning",
        "Heck no, labs are boring.",
        "No, I don't want drugs.",
        "Gimme research.",
        "No, I don't like moving parts.",
        "No, robots.",
        "I like broad",
        "Computers",
        "Yeah bro",
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
        else: #no like buildings
            printQuestion (arrQ[5], arrA[5],arrB[5])
            userInput = getMCPick()
            if userInput == 'A': #yes lab
                printQuestion (arrQ[6], arrA[6],arrB[6])
                userInput = getMCPick()
                if userInput == "A": #yes medicine
                    print ("You belong in Biomedical Engineering")
                else:
                    printQuestion (arrQ[7], arrA[7],arrB[7])
                    userInput = getMCPick()
                    if userInput == 'A': #broad
                        print ("You belong in Chemical Engineering")            
                    else:
                        print ("You belong in Nanotechnology Engineering")
            else: #no lab
                printQuestion (arrQ[8], arrA[8],arrB[8])
                userInput = getMCPick()
                if userInput == 'A': 
                    printQuestion (arrQ[9], arrA[9],arrB[9])
                    userInput = getMCPick()
                    if userInput == 'A':
                        print ("You belong in Mechatronics Engineering")
                    else:
                        print ("You belong in Mechanical Engineering")
                else:
                    printQuestion (arrQ[10], arrA[10],arrB[10])
                    userInput = getMCPick()
                    if userInput == 'A': #hardware
                        printQuestion (arrQ[11], arrA[11],arrB[11])
                        userInput = getMCPick()
                        if userInput == 'A': #power
                            print ("You belong in Electrical Engineering")
                        else: #computer
                            print ("You belong in Computer Engineering")
                    else: #broad
                        printQuestion (arrQ[12], arrA[12],arrB[12])
                        userInput = getMCPick()
                        if userInput == 'A': #syde
                            print ("You belong in Systems Design Engineering")
                        else: #biomed
                            print ("You belong in Biomedical Engineering")
                        

                        


            


