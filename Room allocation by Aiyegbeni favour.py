# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 21:11:07 2021

@author: User
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 18:21:54 2021

@author: User
"""

# dashboard
#Favour Aiyegbeni Victoria
#This project is known as the NUTM project

"""
 The Project is for allocating rooms and providing basic information to scholars
"""


from random import randint
import datetime

def randomGenerator():
    value = randint(1, 60)

    return value

def inputdata():
    dateofexit= "31/09/21"
    name=input("\nEnter your name:")
    checkindate = input("\nEnter your check in date (dd/mm/yy):")
    phonenumber = input("\nEnter your phone number:")
    generatedNum = randomGenerator()
    
    if generatedNum % 2 == 0:
        roomCategory = "A"
    else:
        roomCategory = "B"
    
    
    roomNumValidate = str(generatedNum) + roomCategory
    roomNumList = []
    try:
        roomNumList.index(roomNumValidate)
    except ValueError:
        roomNumList.append(roomNumValidate)
        roomNum = roomNumValidate      #this set of codes is to ensure that each scholar gets a unique roomnumber 
    
    checkindate = date(checkindate)

    idnumber = randint(1020001, 1020060)
    
    print("\nYour room no.:",roomNum,"\n")
    print("Your I.D No:",idnumber,"\n")
    
    return [name, phonenumber, roomNum, checkindate, dateofexit]
        
def roomInfor():
    print("Your can find the following items in your room: ")
    print("1. A bed and two pillows")
    print("2. A workstation containing a table and a chair")
    print("3. A Wardrobe")
    print("4. Kitchen Cabinets with spaces for fridge and microwave")
    print("5. Basic cuttlery like fork, spoon, plate and teacup")
    print("6. A bathroom and toilet to be shared with your roomate")
   
    
def studentlounge():
    breakfast = ["Bread and Tea", "Potato/Yam/Plantain with egg", "French toast", "Pancakes with hotdog and egg"]
    lunch = ["Jollof Rice with chicken/beef/fish",  "Fried rice with beef/fish/chicken", "Pounded Yam with Efo/Egusi", "Eba with Efo/Egusi"]
    dinner = ["White Rice with Stew/fish/beef/chicken","Beans and plantain", "Porridge with beef/fish/chicken"]
    options = int(input("Enter 1 to view the breakfast menu \n Enter 2 to view the lunch menu \n Enter 3 to view the dinner menu"))
    
    if options == 1:
        print("For today`s breakfast we have: ")
        for i in range(len(breakfast)):
            print(str(breakfast[i]) + "\n")
        print("After making your choice kindly call phone number 2030 to place your order")
    if options == 2:
        print("Today's lunch menu consists of: ")
        for i in range(len(lunch)):
            print(str(lunch[i]) + "\n")
        print("After making your choice kindly call phone number 2030 to place your order")
    if options == 3:
        print("Today's dinner menu consists of: ")
        for i in range(len(dinner)):
            print(str(dinner[i]) + "\n")
        print("After making your choice kindly call phone number 2030 to place your order")
    if options > 3:
        print("You have entered the wrong option")
def date(date_string):
    try:
        datetime.datetime.strptime(date_string, "%d/%m/%y")
        return date_string
    except ValueError:
        checkindate=input("\nEnter date in this format: dd/mm/yy :")
        return date(checkindate)
    
   

def Home():
    print ("\n\n A WARM WELCOME TO YOU OUR DEAR NSP SCHOLARS\n WE ARE EXCITED TO HAVE YOU HERE\n")
    print ("To ensure that you are well settled we have created this to make the process easy\n")
    print ("Kindly select your choice by entering the keys for example type 1 for allocation\n")
    add = []
    running = True
    while (running):
        print("1. Hostel and Id Allocation")
        
        print("2. Hostek Rooms Information")

        print("3. Room Service")

    
        print("4. Records")

        print("5. EXIT OPTIONS")

        thechoice=int(input("\nEnter your choice by using the keys e.g enter 1 for Hostel Allocation"))
       
        if (thechoice==1):
            add.append(inputdata())
        if (thechoice==2):
            roomInfor()
        if (thechoice==3):
            studentlounge()
    
        if (thechoice==4):
            print(len(add))
            for i in range(len(add)):
                print(str(i+1) + ". " + "Name: " + add[i][0] + " Phone No: " + add[i][1], " Room No: " + add[i][2] + " Checked-in: " + add[i][3] + "checked-out: " + add[i][4])
          
        if (thechoice==5):
            running= False
        if (thechoice>5):
            print("the option is invalid")
            
        print("\n")

Home()