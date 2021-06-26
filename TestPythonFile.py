#import tkinter as Tk
#from tkinter.ttk import Frame

arrQ = ["Do you like hands on work or programming?",
                 "",
                 ""]

arrA = ["Hate programming, gimme the hands on stuff",
          "",
          ""]

arrB = ["Programming master race",
          "",
          ""]

arrComment = ["",
              "",
              ""]

#procedures
def printQuestion(Q,A,B):        #procedure to print the question
    print(Q)                     #prints question
    print("Option A:", A)        #prints option A
    print("Option B:", B)        #prints option B
    
def getMCPick():
    while True:
        choice = input("Please enter either A or B: ")
        if choice == 'A' or choice == 'a' or choice == 'B' or choice == 'b':        
            break
        else:
            print ("Please only enter A or B")    
    return choice

#obtain user info
userName = str(input("Please enter your name: "))   #asks for user name

print ("Welcome,", userName, "to the Engineering Program selector.") #prints name in a welcome message

while True:
    try:
        userGrade = int(input("Please enter your Grade as a number: "))
        break
    except: 
        print ("Please enter a number.")

printQuestion(arrQ[0],arrA[0],arrB[0])
userInput = getMCPick()
