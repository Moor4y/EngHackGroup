#Data Storing 
arrQ = ["What is your learning style?",    #array to store question information
        "Would you like to work in the natural environment?",
        "Like studying rocks and dirt?",
        "Would you like to work with buildings and infrastructure?",
        "Do you prefer artistic design or structural planning?",
        "Would you like to work in a lab or [blank]?",
        "How about medicine?",
        "Would you prefer working in research and development or keeping your options open?",
        "Are you interested in creating moving parts that work together?",
        "Like robots?",
        "Would you like to focus on hardware and technology or do you have a wider range of engineering interests?",
        "Would you like to work with computer parts or with power and energy?",
        "Medicine?",
        "Are you interested in the business side of engineer?",
        "Do you want to primarily work with computers and devices?",
        "Do you prefer hardware or software?",
        "Would you like to work in a specific area or do you have a broad range of interests?",
        "Medicine?",
        "Do you want to work in artistic design applications to engineering?",
        "Do you enjoy research and analysis or do you prefer a wider range of applications?",
        "Not the program for you? Take the quiz again!"
         ]

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
        "Business = Big $$$",
        "I love learning about computers.",
        "Hardware FTW",
        "Broader the better",
        "I need medicine",
        "Artistic design suits me",
        "Research sounds awesome",
        "Yesss, let's go again"
        ]
        
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
        "Nah, I don't like business.",
        "Nah, computers are overrated.",
        "Software is lit",
        "Specializing is my specialty",
        "I no like medicine",
        "No artistic design for me",
        "I want a wider range of applications",
        "Nah, I'm satisfied."
        ]
arrProgram = ["You belong in Geological Engineering.",      #array to store program information
              "You belong in Environmental Engineering.",
              "You belong in Architectural Engineering",
              "You belong in Civil Engineering",
              "You belong in Electrical Engineering",
              "You belong in Computer Engineering",
              "You belong in Systems Design Engineering",
              "You belong in Biomedical Engineering",
              "You belong in Mechatronics Engineering",
              "You belong in Mechanical Engineering",
              "You belong in Nanotechnology Engineering",
              "You belong in Chemical Engineering",
              "You belong in Software Engineering",
              "You belong in Management Engineering",
              ]

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

def printSpace ():
    for counter in range(0, 3):
        print ("")

#obtain user info
userName = str(input("Please enter your name: "))                    #asks for user name
print ("Welcome,", userName, "to the Engineering Program selector.") #prints name in a welcome message
printSpace ()

#error checking student Grade
while True:
    try:
        userGrade = int(input("Please enter your Grade as a number.\n"
        + "If you are in university, please enter 0: "))
        printSpace ()
        break
    except: 
        print ("Please enter a number.")
        printSpace ()
if userGrade <= 12 and userGrade >= 1:
    print ("Great job of researching your post-secondary options!")
elif userGrade == 0:
    print ("Why are you doing this quiz if you already have a major? Get a life!")
    printSpace ()

userExit = True

while userExit:
    printQuestion(arrQ[0],arrA[0],arrB[0])
    userInput = getMCPick()
    printSpace ()

    #branch 1
    if userInput == 'A': #hands on
        printQuestion(arrQ[1],arrA[1],arrB[1])
        userInput = getMCPick()
        printSpace ()
        if userInput == 'A': #love nature
            printQuestion(arrQ[2],arrA[2],arrB[2])
            userInput = getMCPick()
            printSpace ()
            if userInput == 'A': #love rocks:
                print (arrProgram[0])
            else: #no rocks
                print (arrProgram[1]) 
        else: #no like nature
            printQuestion (arrQ[3], arrA[3],arrB[3])
            userInput = getMCPick()
            printSpace ()
            if userInput == 'A': #love buildings
                printQuestion (arrQ[4], arrA[4],arrB[4])
                userInput = getMCPick()
                printSpace ()
                if userInput == 'A':
                    print (arrProgram[2])
                else:
                    print (arrProgram[3])
            else: #no like buildings
                printQuestion (arrQ[5], arrA[5],arrB[5])
                userInput = getMCPick()
                printSpace ()
                if userInput == 'A': #yes lab
                    printQuestion (arrQ[6], arrA[6],arrB[6])
                    userInput = getMCPick()
                    printSpace ()
                    if userInput == "A": #yes medicine
                        print (arrProgram[7])
                    else:
                        printQuestion (arrQ[7], arrA[7],arrB[7])
                        userInput = getMCPick()
                        printSpace ()
                        if userInput == 'A': #broad
                            print (arrProgram[11])
                        else:
                            print (arrProgram[10])
                else: #no lab
                    printQuestion (arrQ[8], arrA[8],arrB[8])
                    userInput = getMCPick()
                    printSpace ()
                    if userInput == 'A': 
                        printQuestion (arrQ[9], arrA[9],arrB[9])
                        userInput = getMCPick()
                        printSpace ()
                        if userInput == 'A':
                            print (arrProgram[8])
                        else:
                            print (arrProgram[9])
                    else:
                        printQuestion (arrQ[10], arrA[10],arrB[10])
                        userInput = getMCPick()
                        printSpace ()
                        if userInput == 'A': #hardware
                            printQuestion (arrQ[11], arrA[11],arrB[11])
                            userInput = getMCPick()
                            printSpace ()
                            if userInput == 'A': #power
                                print (arrProgram[4])
                            else: #computer
                                print (arrProgram[5])
                        else: #broad
                            printQuestion (arrQ[12], arrA[12],arrB[12])
                            userInput = getMCPick()
                            printSpace ()
                            if userInput == 'A': #syde
                                print (arrProgram[6])
                            else: #biomed
                                print (arrProgram[7])
    else: #hands off
        printQuestion(arrQ[1],arrA[1],arrB[1])
        userInput = getMCPick()
        printSpace ()
        if userInput == 'A': #love nature
            printQuestion(arrQ[2],arrA[2],arrB[2])
            userInput = getMCPick()
            printSpace ()
            if userInput == 'A': #love rocks:
                print (arrProgram[0])
            else: #no rocks
                print (arrProgram[1])
        else:                    
            printQuestion(arrQ[13],arrA[13],arrB[13])
            userInput = getMCPick()
            printSpace ()
            if userInput == 'A': #yes business
                print (arrProgram[13])
            else:
                printQuestion(arrQ[14],arrA[14],arrB[14])
                userInput = getMCPick()
                printSpace ()
                if userInput == 'A': #yes computers 
                    printQuestion(arrQ[15],arrA[15],arrB[15])
                    userInput = getMCPick()
                    printSpace ()
                    if userInput == 'A': #hardware
                        print (arrProgram[5])
                    else: 
                        print (arrProgram[12])
                else:
                    printQuestion(arrQ[16],arrA[16],arrB[16])
                    userInput = getMCPick()
                    printSpace ()
                    if userInput == 'A': #broad
                        printQuestion(arrQ[17],arrA[17],arrB[17])
                        userInput = getMCPick()
                        printSpace ()
                        if userInput == 'A': #yes medicine
                            print (arrProgram[7])
                        else: 
                            print (arrProgram[6])
                    else: 
                        printQuestion(arrQ[18],arrA[18],arrB[18])
                        userInput = getMCPick()
                        printSpace ()
                        if userInput == 'A': #yes artistic design
                            print (arrProgram[2])
                        else:
                            printQuestion(arrQ[19],arrA[19],arrB[19])
                            userInput = getMCPick()
                            printSpace ()
                            if userInput == 'A': #research
                                print (arrProgram[10])
                            else:
                                print (arrProgram[11])
    
    printQuestion(arrQ[20],arrA[20],arrB[20])
    userInput = getMCPick()
    printSpace ()
    if userInput == 'A': #encore
        print ("Reinitiating the quiz...")    
        printSpace ()
    else:
        print ("Have a nice day!")
        userExit = False

