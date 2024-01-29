import random
import sys
import time
from os import system, name
import core
import campic
import foxRun
from scares import foxy, bonnie, chica, fredCool

#TODO add movement timers to make animatronics stay in place for at least 2 turns

minute = 1
hour = 0
power = 1000

bonPos = 0
bonThreat = 0
bonStag = 0
bonOp = 0

chiPos = 0
chiThreat = 0
chiStag = 0
chiOp = 0

foxPos = 0
foxTime = 100
foxToken = False

preGold = 0
goldToken = False
postGold = 0

count = 0
action = None
cam = None

lDoor = False
rDoor = False

def threat(hour, bstag, cstag):
    if(hour == 0):
        rollb = (random.randint(1,50) + bstag)
        rollc = (random.randint(1,50) + cstag)
    else:
        rollb = ((random.randint(1,50) + bstag) * hour)
        rollc = ((random.randint(1,50) + cstag) * hour)
    return rollb, rollc

def SPrint(pause, string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(pause)

def rareRoll(chance):
    return random.randint(0,chance)

def gold():
    while True:
        rand = random.randint(0,4)
        if(rand == 0):
            campic.goldFlash()
        elif(rand == 1):
            campic.goldSprite()
        elif(rand == 2):
            campic.goldFull()
        elif(rand == 3):
            campic.goldLimp()
        else:
            campic.goldStare()
        time.sleep(0.0416)

core.clear()
SPrint(0.00025,"""Hello? Hello, hello? Uh, I wanted to record a message for you to help you get settled in on your first night. Um, I actually worked in that office before you. I'm finishing up my last week now, as a matter of fact. So, I know it can be a bit overwhelming, but I'm here to tell you there's nothing to worry about. Uh, you'll do fine. So, let's just focus on getting you through your first week, okay?
Uh, let's see, first there's an introductory greeting from the company that I'm supposed to read. Uh, it's kind of a legal thing, you know. Um, "Welcome to Freddy Fazbear's Pizza. A magical place for kids and grown-ups alike, where fantasy and fun come to life. Fazbear Entertainment is not responsible for damage to property or person. Upon discovering that damage or death has occurred, a missing person report will be filed within 90 days, or as soon property and premises have been thoroughly cleaned and bleached, and the carpets have been replaced."

Blah, blah, blah. Now that might sound bad, I know, but there's really nothing to worry about. Uh, the animatronic characters here do get a bit quirky at night, but do I blame them? No. If I were forced to sing those same stupid songs for twenty years and I never got a bath? I'd probably be a bit irritable at night too. So, remember, these characters hold a special place in the hearts of children and we need to show them a little respect, right? Okay.

So, just be aware, the characters do tend to wander a bit. Uh, they're left in some kind of free roaming mode at night. Uh... something about their servos locking up if they get turned off for too long. Uh, they used to be allowed to walk around during the day too. But then there was The Bite of '87. Yeah. I-It's amazing that the human body can live without the frontal lobe, you know?

Uh, now concerning your safety, the only real risk to you as a night watchman here, if any, is the fact that these characters, uh, if they happen to see you after hours probably won't recognize you as a person. They'll pr- they'll most likely see you as a metal endoskeleton without its costume on. Now since that's against the rules here at Freddy Fazbear's Pizza, they'll probably try to... forcefully stuff you inside a Freddy Fazbear suit. Um, now, that wouldn't be so bad if the suits themselves weren't filled with crossbeams, wires, and animatronic devices, especially around the facial area. So, you could imagine how having your head forcefully pressed inside one of those could cause a bit of discomfort... and death. Uh, the only parts of you that would likely see the light of day again would be your eyeballs and teeth when they pop out the front of the mask, heh.

Y-Yeah, they don't tell you these things when you sign up. But hey, first day should be a breeze. I'll chat with you tomorrow. Uh, check those cameras, and remember to close the doors only if absolutely necessary. Gotta conserve power. Alright, good night.
""")
input("Press Enter to Start")
core.clear()
while hour < 6:
    if(power <= 0):
        break
    count += 1 #Used to insert the 0 before single digit numbers in the minutes place
    if(minute%60 == 0):
        hour += 1
        count = 0
    if(count < 10):
        print("Time : " + str(hour) + ":0" + str(minute%60))
    else:
        print("Time : " + str(hour) + ":" + str(minute%60))
    print("Power : " + str(power))
    while(not action in ["c","ll","ld","rl","rd","n","m","ftest","btest","ctest","die","tcheck","gtest","win"]): #error correcting list of possible actions
        print("###################################################################################################################################################")
        print("# c : Check cameras | ll : Check left light | ld : Toggle left door | rl : Check right light | rd : Toggle Right Door | n : Do nothing, pass time #")
        print("###################################################################################################################################################")
        action = input("What would you like to do? : ") #User decides what action to do for thier turn.
        core.clear()
        if(goldToken == True):
            if(rareRoll(9) == 9):
                campic.goldFlash()
                postGold += 1

    if(action == "c"): #User is checking a camera
        preGold += 1 # If the player does nothing but check cameras they will eventually encounter Golden Freddy
        power -= 1
        while(not cam in ["1a","1b","1c","2a","2b","3","4a","4b","5","6","7"]): # Error correcting list of possible cameras
            campic.map()
            print("""1a  : Stage
1b  : Dining Hall
1c  : Pirate's Cove
2a  : Northwest Hall
2b  : SouthWest Hall
3   : Supply Closet
4a  : Northeast Hall
4b  : Southeast Hall
5   : Backstage
6   : Kitchen
7   : Bathroom Hall""")
            cam = input("Which camera? : ") # User decides which camera to check
            if(cam == "1a"): # Check stage camera
                if(bonPos == 0 and chiPos == 0):
                    if(rareRoll(9) == 9):
                        campic.stageAllLook()
                    else:
                        campic.stageAll()
                elif(bonPos == 0 and chiPos != 0):
                    campic.stageFBX()
                elif(bonPos != 0 and chiPos == 0):
                    campic.stageFXC()
                else:
                    campic.stageFXX()
            elif(cam == "1b"):    # Check dining room camera
                if(bonPos == 2 and chiPos == 1):
                    chiPos -= 1
                if(bonPos == 2):
                    campic.diningBX()
                elif(chiPos == 1):
                    campic.diningXC()
                else:
                    campic.diningXX()
            elif(cam == "1c"):    # Check Foxy camera
                if(foxTime > 75):
                    campic.coveClosed()
                    print("The curtain is closed in Pirate's Cove.")
                elif(foxTime > 30):
                    campic.covePeek()
                    print("Foxy Peeking Through Cutain")
                elif(foxTime > 0):
                    campic.coveWalk()
                    print("Foxy Out of Curtains")
                else:
                    campic.coveGone()
                    print("Foxy Gone")
                if(foxToken == False):
                    foxTime += 10
                    if(foxTime > 100):
                        foxTime = 100
            elif(cam == "2a"): # Far left hall camera
                if(foxPos == 2 and bonPos ==3):
                    bonPos -= 1
                if(foxPos == 2):
                    foxRun.fRun()
                if(bonPos == 3):
                    campic.lHallFarB()
                else:
                    campic.lHallFarX()
            elif(cam == "2b"):
                if(bonPos == 5): # Close left hall camera
                    campic.lHallCloseB()
                elif(goldToken == True):
                    campic.lHallCloseG()
                else:
                    campic.lHallCloseX()
            elif(cam == "3"): # Supply closet camera
                if(bonPos == 4):
                    campic.supplyB()
                else:
                    campic.supplyX()
            elif(cam == "4a"): # Far right hall camera
                if(chiPos == 3):
                    campic.rHallFarC()
                else:
                    campic.rHallFarX()
            elif(cam == "4b"): # Close right hall camera
                if(chiPos == 5):
                    campic.rHallCloseC()
                else:
                    campic.rHallCloseX()
            elif(cam == "5"): # Backstage camera
                if(bonPos == 5):
                    campic.backstageB()
                else:
                    campic.backstageX()
            elif(cam == "6"): # Kitchen camera with audio only
                print("""*NO VIDEO*
                *AUDIO ONLY*""")
                if(chiPos == 4):
                    print("You hear the rustling of pots and pans")
                else:
                    print("Nothing can be heard")
            elif(cam == "7"): # Outside of bathrooms camera
                if(chiPos == 2):
                    campic.restroomC()
                else:
                    campic.restroomX()
            #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^# End of camera action



    elif(action == "rd"): # Right door toggle
        if(rDoor == True):
            rDoor = False
            print("Right door opened")
        else:
            rDoor = True
            print("Right door closed")

    elif(action == "ld"): # Left door toggle
        if(lDoor == True):
            lDoor = False
            print("Left door opened")
        else:
            lDoor = True
            print("Left door closed")

    elif(action == "rl"): # Right light check
        if(chiPos == 7):
            campic.rLightC()
            print("Chica is at the door.")
        else:
            print("You spot nothing in the window")
        power -= 1

    elif(action == "ll"): # Left light check
        if(bonPos == 7):
            campic.lLightB()
            print("Bonnie is at the door.")
        else:
            print("You spot nothing in the window")
        power -= 1

    elif(action == "n"): # Do nothing, pass time.
        print("Time passes...")

#VVVVVVVVV Test Actions VVVVVVVVVVV
    if(action == "ftest"):
        fredCool()
    if(action == "btest"):
        bonnie()
    if(action == "ctest"):
        chica()
    if(action == "gtest"):
        gold()
    if(action == "die"):
        power = 5
    if(action == "win"):
        hour = 5
        minute = 55
###################################### End of Actions

#VVVVVVVVVVVVVVV# Main animatronic AI #VVVVVVVVVVVVVVV#

    if(bonPos in [0,3]): # Checking if Bonnie is in position to take optional path
        bonOp = 1
    elif(bonPos in [1,4]): # Checking if Bonnie is in a dead-end optional path
        bonOp = 2
    else:
        bonOp = 0 # Bonnie is on the regular path

    if(chiPos in [1,3]): # Checking if Chica is in position to take optional path
        chiOp = 1
    elif(chiPos in [2,4]): # Checking if Chica is in a dead-end optional path
        chiOp = 2
    else:
        chiOp = 0 # Chica is on a regular path

    [bonThreat, chiThreat] = threat(hour, bonStag, chiStag) # Bonnie and Chica's threat is generated.

#VVVVVVVVVVVVVVV# Bonnie AI #VVVVVVVVVVVVVVV#

    if(bonOp == 1): # Bonnie can now reset, stay, go into an optional dead-end path, or progress.
        if(bonThreat < 26):
            if(bonPos != 0):
                if(bonPos > 2):# Bonnie can reset if past the Dining Hall
                    bonPos = 0
                    bonStag = 1
            print("Bonnie Reset")
        elif(25 < bonThreat < 51):
            print("Bonnie stays still")
            bonStag += 1
        elif(50 < bonThreat < 76):
            print("Bonnie moves into optional")
            bonPos += 1
            bonStag = 0
        else:
            print("Bonnie moves forward, skipping optional path")
            bonPos +=2
            bonStag = 0
    elif(bonOp == 2):# Bonnie can now reset, stay, or get out of the optional dead-end path
        if(bonThreat < 26):
            if(bonPos != 0):
                if(bonPos > 2):# Bonnie can reset if past the Dining Hall
                    bonPos = 0
                    bonStag = 1
                    print("Bonnie Reset")
        elif(bonThreat < 76):
            bonPos -= 1
            bonStag = 0
            print("Bonnie exits dead-end")
        else:
            print("Bonnie stays still")
            bonStag += 1
    elif(bonOp == 0):# Bonnie can now reset, stay, or progress
        if(bonThreat < 34):
            if(bonPos != 0):
                if(bonPos > 2):# Bonnie can reset if past the Dining Hall
                    bonPos = 0
                    bonStag = 1
                    print("Bonnie Reset")
        elif(bonThreat < 67):
            bonStag += 1
            print("Bonnie stays still")
        else:
            print("Bonnie progresses")
            bonPos += 1
            bonStag = 0

    if(bonPos == 8): # Bonnie is at the door. If it is closed, he remains outside. If it is open, the player dies
        if(lDoor == True):
            bonPos = 7
        else:
            bonnie()

#VVVVVVVVVVVVVVV# Chica AI #VVVVVVVVVVVVVVV#

    if(chiOp == 1): # Chica can now reset, stay, go into an optional dead-end path, or progress
        if(chiThreat < 26):
            if(chiPos != 0):
                if(chiPos > 2):# Chica can reset if past the Dining Hall
                    chiPos = 0
                    chiStag = 1
                    print("Chica Reset")
        elif(25 < chiThreat < 51):
            print("Chica stays still")
            chiStag += 1
        elif(50 < chiThreat < 76):
            print("Chica moves into optional")
            chiPos += 1
            chiStag = 0
        else:
            print("Chica moves forward, skipping optional path")
            chiPos +=2
            chiStag = 0
    elif(chiOp == 2):# Chica can now reset, stay, or get out of the optional dead-end path
        if(chiThreat < 26):
            if(chiPos != 0):
                if(chiPos > 2):# Chica can reset if past the Dining Hall
                    chiPos = 0
                    chiStag = 1
                    print("Chica Reset")
        elif(chiThreat < 76):
            chiPos -= 1
            chiStag = 0
            print("Chica exits dead-end")
        else:
            print("Chica stays still")
            chiStag += 1
    elif(chiOp == 0):# Chica can now reset, stay, or progress
        if(chiThreat < 34):
            if(chiPos != 0):
                if(chiPos > 2):# Chica can reset if past the Dining Hall
                    chiPos = 0
                    chiStag = 1
                    print("Chica Reset")
        elif(chiThreat < 67):
            chiStag += 1
            print("Chica stays still")
        else:
            print("Chica moves forward")
            chiPos += 1
            chiStag = 0

    if(chiPos == 8): # Chica is at the door. If it is closed, she remains outside. If it is open, the player dies
        if(rDoor == True):
            chiPos = 7
        else:
            chica()
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV# Post player-action calculations

    if(lDoor == True): # Doors drain power if closed
        power -= 2
    if(rDoor == True):
        power -= 2

    if(action != "c"): # Player didn't check cameras this turn, postponing the Golden Freddy trigger
        preGold -= 10
    if(preGold < 0):
        preGold = 0

    if(cam != "1c"): # If the player doesn't check camera 1c, Foxy's camera, Foxy's timer goes down. the timer goes down faster later in the night.
        if(hour == 0):
            foxTime -= 1
        else:
            foxTime -= hour

    power -= 1 # Ambient power drain
    minute += 1 # Time passing
    action = None # Resetting user input for the next turn
    cam = None

    if(preGold == 25):
        goldToken = True

    if(postGold == 10):
        gold()

    if(foxPos > 2): # Foxy is at the door. If it is closed he remains outside and pounds on the door, draining power then resetting. If it is open, the player dies.
        if(lDoor == True):
            power -= 25
            print("You hear a loud slamming noise on the door to your left, then footsteps going down the hall")
            foxToken = False
            foxTime = 50
            foxPos = 0
        else:
            foxy()

    if(foxToken == True): # Foxy approacing if his timer ends.
        foxPos += 1

    if(foxTime <= 0): #Checking if Foxy is gone
        foxToken = True

    print("++++++++++++++++++++")
    print("Power            : " + str(power))
    print("Foxy Timer       : " + str(foxTime))
    print("Foxy Token       : " + str(foxToken))
    print("Foxy Position    : " + str(foxPos))
    print("Cam              : " + str(cam))
    print("Chica Threat     : " + str(chiThreat))
    print("Chica Op         : " + str(chiOp))
    print("Chica Stagnation : " + str(chiStag))
    print("Chica Position   : " + str(chiPos))
    print("Bonnie Threat    : " + str(bonThreat))
    print("Bonnie Op        : " + str(bonOp))
    print("Bonnie Position  : " + str(bonPos))
    print("Bonnie stagnation: " + str(bonStag))
    print("Pre-Gold         : " + str(preGold))
    print("Gold Token       : " + str(goldToken))
    print("Post-Gold        : " + str(postGold))
    print("--------------------")


if (hour == 6):
    SPrint(0.05,"""⣉⣭⣭⣭⣭⣭⡭⠭⠭⠭⠭⠬⠭⠥⠭⠍⠉⠉⠉⠉⠉⠭⠭⠭⠥⠤⠤⠭⠥⠭⠬⠥⠭⠬⠥⠭⠭⠍⠉⠛⢛⣉⣉⣉⣉⣉⣉
⣿⣿⣿⣿⣿⣿⣟⢢⠐⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠠⠀⢀⢻⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡿⢎⠣⢌⠠⠁⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣴⣶⡶⠿⠟⠻⢦⣦⠐⠀⠌⣿⣿⣿⣿⡗
⣿⣿⣿⣿⣿⡷⣉⠗⡨⣰⣆⣤⣠⣄⣤⣀⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⣤⠞⣟⣻⣭⠤⠴⣤⣔⣈⠤⠉⠆⡁⠈⣽⣿⣿⠋⠀
⣿⣿⣿⣿⣿⣗⠮⣽⣿⣿⡿⢿⢿⣿⣿⣿⣿⣿⡿⣶⣆⠀⠀⠀⠀⠀⠩⠀⣾⡯⢿⡿⣿⡗⣶⣮⡝⡂⢁⠂⠄⠐⣸⣿⡇⠈⠀
⣸⣿⣿⣿⣿⣯⢺⣿⣿⡹⣾⣿⣿⠻⣿⣟⡿⠙⣽⠊⢏⠆⠀⠀⠀⠀⠁⠀⠘⠀⠀⠉⠉⡀⠆⠉⠁⠀⠀⠀⢀⠂⣸⡿⢃⠀⠀
⢿⣿⣿⣻⣿⣷⡉⢯⠘⡙⠙⠿⣋⠓⡀⢀⠀⠄⠀⠀⠀⠎⠀⠀⠀⠀⠀⠀⠀⠀⠁⠈⠀⠀⠀⠀⠀⠀⠀⠀⢀⠠⢸⢃⠀⢀⠀
⣼⢣⣿⣽⣿⣷⡍⠦⡁⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠌⡐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠂⣹⠃⠀⢀⠀
⣿⣇⢾⣷⡿⣿⣯⡓⠤⢁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢂⠄⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠎⡏⠀⢀⠜⣰
⣿⣿⣿⣿⣷⣻⣿⣷⢞⢠⠀⠆⠀⠀⠀⠀⠀⠀⠀⢘⠀⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⢘⣧⣴⡞⣰⣷
⣿⣿⣿⣿⣿⣿⣻⡿⣎⠀⢃⠀⠀⠀⠀⠀⠀⠀⠀⣈⠀⠆⠀⠀⠀⠀⢀⡀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠃⠎⣿⠟⢰⣿⣻
⣿⣿⣿⣿⣿⣿⣿⣿⣎⡜⠠⠀⠄⠀⠀⠀⠀⠀⠀⠸⣾⣿⣿⣧⠠⣤⣿⡿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠠⠐⢈⡏⣰⣿⣳⣿
⣿⣿⣿⣿⣿⣿⣿⣿⢦⡙⣆⢁⠂⠄⠂⠀⠀⠀⠀⠀⠀⠉⠉⠛⠟⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠠⡇⢻⣿⡿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣧⠘⡄⠣⡌⠠⢀⠀⢄⣠⡀⢄⣀⣀⣀⣀⠀⣀⣀⣄⣀⣠⣤⠶⠀⠀⠀⠀⠠⠀⠀⠀⠀⡐⣷⣈⠻⠿⠷
⣿⣿⣿⣿⣿⣿⣿⣿⣷⡩⢐⠡⠸⣄⠀⠈⠀⠉⠙⠛⠛⠙⠉⠋⠛⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠐⠀⠀⠀⠀⠁⣼⣿⣧⡵⢒⡑
⠱⣋⠿⣿⣿⣿⣿⣿⣿⣗⢣⠌⡡⠘⡆⢀⠀⠀⡀⠂⠁⠄⠠⣀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⢀⠈⣴⣙⢿⠫⠑⠂⠀
⠀⠈⠈⠑⠛⠿⢿⣿⣿⣿⣷⣎⠤⡑⢌⠢⠀⠄⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠄⡀⢦⣽⠣⡼⠘⠁⢀⠀⠀
⠀⠀⠀⠀⠀⠠⢉⢾⣿⣿⣿⣿⣿⣞⣤⢃⠌⠠⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢀⣶⢿⡟⢥⡳⠁⠀⠠⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠌⣾⣿⣿⣿⣿⣿⣿⣿⣾⣬⣑⠠⢁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⣱⣾⡟⢧⣺⠞⠁⠀⠀⠀⠀⠠⠀
⠀⠀⠀⠀⠀⠀⣘⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣗⣤⢂⠄⡀⢀⠀⡀⢀⠀⡀⠀⣄⣢⣽⣿⣿⢳⡽⠊⠁⠀⠀⠀⠀⠀⠂⠀⠁
⠀⠀⠀⠀⠀⣐⣾⣿⡿⡙⣿⣿⢿⣫⠿⣿⣿⣿⣿⣿⣿⣷⣿⣼⣾⣵⣯⣾⣵⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                     YOU WIN""") # Player wins, game ends

else:
    fredCool()
