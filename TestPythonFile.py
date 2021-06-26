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
arrProgram = ["Based on your responses, we think that you’d be a great fit for geological engineering! Studying soil and rock behaviour is your thing, because you like to solve complex problems around the world no matter what field it’s in! So many choices proven to never be a bore, whether it's working in oil & gas, mineral exploration, hazard waste removal, or groundwater management and lots more!",      #array to store program information
              "Based on your responses, we think that you’d be a great fit for environmental engineering! Studying bacterial culture and cleansing nasty soil may be gross for others to succumb to, but saving the world is important, and you bear it so they don’t have to! By applying for this degree at the University of Waterloo, you can be a part of the nation’s largest Environmental Engineering program. Learn how to make a societal change by tackling the technical aspects of environmental problems we experience today. Your insight into the details around pollution and other environmental-issues can create a long-lasting impact on policy and the future of this planet.",
              "Based on your responses, we think that you’d be a great fit for architectural engineering! Develop  innovative structures , renovate ancient archives, let your creative juices run their course, all the while building a better and brighter future for yourself. Need even more homes in the KW region? Want to continue to skyrocket property prices in Canada? No problem, this program that is based on designing, renovating, and ensuring the sustainability of buildings will help you do just that. Your passion for a mixture of the arts and that technical side of engineering will play a great role in your success in this field!",
              "Based on your responses, we think that you’d be a great fit for civil engineering! Bulldoze your way into designing  and maintaining the massive infrastructure we all depend on, and who knows, maybe after test driving through the different career aspects, you might just be the person who at last saves  the London Bridge from falling down! Become a part of Canada’s largest  and the world’s top 100  civil engineering program,  by at the University of Waterloo, and make your hometown your oyster! In other words, your knowledge can take you to work for a variety of construction, infrastructure, and transportation companies, as well as the government itself to plan and maintain the systems that keep our city on the move.",
              "Based on your responses, we think that you’d be a great fit for electrical engineering! Mess with wires, play with instrumentation,  or make a polling generator, you're sure to find an electrical engineer at the base of any information, power, and energy change maker! Feel the power in your grasp to be a part of the world’s best programs in the field. You are someone who is interested in harnessing the core energy source that powers our devices and the systems that improves the lives of millions. Your hands-on skills will be invaluable as you will be working with circuits and wires, but your technical knowledge will also help guide you through the rigorous engineering and math courses needed for the degree.",
              "Based on your responses, we think that you’d be a great fit for computer engineering! Wanna create the next generation’s Twitch? Or Create hardware for a quantum computer? Why yes you may, as long as your code is neater,  dream on and dream big because you'll never have to worry about taxes, when you are filthy rich! Your passion for technology shines through in this degree, with many specializations available in both hardware and software roles! You will gain thorough knowledge about all aspects of computers, from their internal parts to the complex software giving them their functionality.",
              "You belong in Systems Design Engineering",
              "Based on your responses, we think that you’d be a great fit for biomedical engineering! Designing bionic limbs to help Usain Bolt run faster gets you excited, but dealing directly with sick patients leaves you frightened? This is the program for you! Create the newest medical solutions with advanced technologies in biomedical engineering.",
              "Based on your responses, we think that you’d be a great fit for mechatronics engineering! From  the biometric train station down the street, or the old ATM machine that's now dead beat, to the automated cashiers at the checkout counter, computer-controlled electromechanical systems will make every human flounder. Combine a variety of disciplines into one program and voila - you have your dream program. This program demands knowledge of software, electronics, and mech, to find success in this field. You dream of making the next smart AI that can walk, talk, do your homework, and complete a ‘tron degree by itself. Just make sure not to start the robot uprising!",
              "Based on your responses, we think that you’d be a great fit for mechanical engineering! You love some good yellow cheese, whether you work on Elon’s spacecraft or make expensive meters HydroOne can’t bill and things that move, make you groove. But mechanics, power, control and manufacturing is your gear’s elbow grease, and impressing employers is your main swell. You have always been itching to use your hands to create something, so let that passion drive you to success! In this degree, you will have the opportunity to work with others to design machines of all sizes and of all functionalities, pursuing the goal of better and more efficient products. Have the power of metal and electricity at your hands and start creating!",
              "Based on your responses, we think that you’d be a great fit for nanotechnology engineering! Would you like to dip your toes in research, collaborating with the great giants? (Harvard, MIT etc.) Take the opportunity to experience Canada’s sole undergraduate program for nanotechnology, an emerging and exciting new field in a world of innovation. By using your knowledge in a variety of fields such as biology, chemistry, and quantum physics, you can be at the forefront of research and development of things that cannot even be seen by the naked eye!",
              "Based on your responses, we think that you’d be a great fit for chemical engineering! You're confident your meth can be bluer than Mr. White's, and launching your skincare brand brings you delight! This field combines a unique blend of chemistry and materials science, which can earn you a placement in the country’s most interesting companies that deal with topics ranging from fuel energy to pharmaceutical companies.",
              "Based on your responses, we think that you’d be a great fit for software engineering! Working in Silicon Valley may seem out of your reach, but developing your own VR software can take you right to the beach!  Enabling businesses to become tech savvy, the burden on your shoulders to analyze software, apply algorithms, understand digital design, human/ computer interfaces, becomes heavy.  Comrade, don't forget, your teammates have always got your back, so you can continue to develop and build the next Snapchat! You are driven by your passion in programming and digital hardware systems, as well as computer algorithms and interfaces. This degree is among the greatest in terms of employability - companies such as Google, Amazon, and Facebook are hungry for smart thinkers like you! Although you may be stereotyped as quiet and independent, that doesn’t stop you from joining the thousands of software engineers like you from being interested in a coveted spot in this program.",
              "Based on your responses, we think that you’d be a great fit for management engineering! Supply chains, fine tuning, data analytics and information systems is what you have mastered, so you make swift moves and have beauractrics flow faster!Making engineering projects run as smoothly as possible is just for you! As a management engineer, you will be a key component in any engineering project, taking charge of the resource and supply management that makes projects efficient and organized. Be your own boss!",
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

