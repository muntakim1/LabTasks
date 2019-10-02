#!/usr/bin/env python3

import datetime,os
#####Global Varibales
choiceAgain=False

def dbHeader(greet,devName,version="default value"):
    print("********{} ({})*********".format(greet.upper(),version))
    print("                      {}                      ".format(devName))
    #print(greet.upper())
    logUpdater("db Header printed.")
    
def chooseMenu():
    print("1. Login")
    print("2. View Result")
    print("3. Print Report Card")
    logUpdater("Choice Menu Showed!")
    global choiceAgain
    choiceList=[0,1,2,3]
    choiceAgain=False
    
    
    while not choiceAgain:
        choice=int(input("Enter your choice: "))
        logUpdater("Waiting for choice.")
        if choice==choiceList[1]:
            logUpdater("Choice entered "+str(choiceList[1]))
            login()
        elif choice==choiceList[2]:
            logUpdater("Choice entered "+str(choiceList[2]))
            viewResult()
        elif choice==choiceList[3]:
            logUpdater("Choice entered "+str(choiceList[3]))
            printReport()
        elif choice==choiceList[0] or choice not in choiceList:
            logUpdater("Choice entered ")
            error()
        
def login():
    print("System logged in")
    logUpdater("System logged in.")
    #global choiceAgain
    global choiceAgain
    choiceAgain=True
    
def viewResult():
    print("View Result")
    logUpdater("View Result.")
    #global choiceAgain
    global choiceAgain
    choiceAgain=True
    
def printReport():
    print("Print Report")
    logUpdater("Print Report.")
    #global choiceAgain
    global choiceAgain
    choiceAgain=True
    
def error():
    logUpdater("Error rised: Invalid choice")
    #global choiceAgain
    print("Invalid Option Choosen.")
    global choiceAgain
    choiceAgain=False
    
#logfile Updater
    
def logUpdater(greet):
    if os.path.isfile("registry.log"): # checking file is exits or not
        f = open("registry.log",'a') # if exits create the file
    else:
        f = open("registry.log",'w+') # if not exits create the file
        
    f.write(str(datetime.datetime.now())+"->"+greet+"\n")
    f.close()



#Main Execution Operations Part
# 1.1 Call the dbHeader Function
greetingMsg="Welcome to Student DB Management System"
swVersion="v 1.01"
devName="Mr.Muntakimur Rahaman"

dbHeader(greetingMsg,devName,swVersion)
chooseMenu()


