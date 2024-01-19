import random
import sys
import time
from os import system, name
import core
import campic
from scares import foxy, bonnie, chica, freddy

minute = 1
hour = 0
power = 1000

bonPos = 0
bonThreat = 0
bonStag = 0

chiPos = 0
chiThreat = 0
chiStag = 0

foxPos = 0
foxTime = 100
foxToken = False

count = 0
action = None
cam = None

lDoor = False
rDoor = False

def threat(hour, stag):
    if(hour == 0):
        roll = (random.randint(1,50) + stag)
    else:
        roll = ((random.randint(1,50) + stag) * hour)
    return roll

def SPrint(string):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.001)

core.clear()
SPrint("""Hello? Hello, hello? Uh, I wanted to record a message for you to help you get settled in on your first night. Um, I actually worked in that office before you. I'm finishing up my last week now, as a matter of fact. So, I know it can be a bit overwhelming, but I'm here to tell you there's nothing to worry about. Uh, you'll do fine. So, let's just focus on getting you through your first week, okay?
Uh, let's see, first there's an introductory greeting from the company that I'm supposed to read. Uh, it's kind of a legal thing, you know. Um, "Welcome to Freddy Fazbear's Pizza. A magical place for kids and grown-ups alike, where fantasy and fun come to life. Fazbear Entertainment is not responsible for damage to property or person. Upon discovering that damage or death has occurred, a missing person report will be filed within 90 days, or as soon property and premises have been thoroughly cleaned and bleached, and the carpets have been replaced."

Blah, blah, blah. Now that might sound bad, I know, but there's really nothing to worry about. Uh, the animatronic characters here do get a bit quirky at night, but do I blame them? No. If I were forced to sing those same stupid songs for twenty years and I never got a bath? I'd probably be a bit irritable at night too. So, remember, these characters hold a special place in the hearts of children and we need to show them a little respect, right? Okay.

So, just be aware, the characters do tend to wander a bit. Uh, they're left in some kind of free roaming mode at night. Uh... something about their servos locking up if they get turned off for too long. Uh, they used to be allowed to walk around during the day too. But then there was The Bite of '87. Yeah. I-It's amazing that the human body can live without the frontal lobe, you know?

Uh, now concerning your safety, the only real risk to you as a night watchman here, if any, is the fact that these characters, uh, if they happen to see you after hours probably won't recognize you as a person. They'll pr- they'll most likely see you as a metal endoskeleton without its costume on. Now since that's against the rules here at Freddy Fazbear's Pizza, they'll probably try to... forcefully stuff you inside a Freddy Fazbear suit. Um, now, that wouldn't be so bad if the suits themselves weren't filled with crossbeams, wires, and animatronic devices, especially around the facial area. So, you could imagine how having your head forcefully pressed inside one of those could cause a bit of discomfort... and death. Uh, the only parts of you that would likely see the light of day again would be your eyeballs and teeth when they pop out the front of the mask, heh.

Y-Yeah, they don't tell you these things when you sign up. But hey, first day should be a breeze. I'll chat with you tomorrow. Uh, check those cameras, and remember to close the doors only if absolutely necessary. Gotta conserve power. Alright, good night.
""")
input("Press Enter to Start")
core.clear()
while hour < 6:
    if(foxTime == 0): #Checking if Foxy is gone
        foxToken = True
    if(power <= 0):
        break
    count += 1 #Used to insert the 0 before single digit numbers in the minutes place
    if(minute%60 == 0):
        hour += 1
        count = 0
    if(count < 10):
        print(str(hour) + ":0" + str(minute%60))
    else:
        print(str(hour) + ":" + str(minute%60))
    print("Power: " + str(power))
    print("Foxy Timer: " + str(foxTime))
    print("Foxy Token: " + str(foxToken))

    while(not action in ["c","ll","ld","rl","rd","n","ftest","btest","ctest","die","tcheck"]): #error correcting list of possible actions
        action = input("What would you like to do? : ") #User decides what action to do for thier turn.

    if(action == "c"): #User is checking a camera
        power -= 1
        while(not cam in ["1a","1b","1c","2a","2b","3","4a","4b","5","6","7"]): #Error correcting list of possible cameras
            cam = input("Which camera? : ") #User decides which camera to check
            print("Put cam info here")
            if(cam == "1c"):
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

    elif(action == "rd"): #Right door toggle
        if(rDoor == True):
            rDoor = False
        else:
            rDoor = True

    elif(action == "ld"): #Left door toggle
        if(lDoor == True):
            lDoor = False
        else:
            lDoor = True

    elif(action == "rl"):
        print("light info")
        power -= 1

    elif(action == "ll"):
        print("light info")
        power -= 1

    elif(action == "n"):
        print("Time passes...")

    if(action == "ftest"):
        foxy()
    if(action == "btest"):
        bonnie()
    if(action == "ctest"):
        chica()
    if(action == "die"):
        power = 5
    if(action == "tcheck"):
        print(threat(hour, bonStag))


    if(lDoor == True):
        power -= 2
    if(rDoor == True):
        power -= 2

    if(cam != "1c"):
        foxTime -= 1
    power -= 1 #Ambient power drain
    minute += 1
    action = None
    cam = None


if (hour == 6):
    print("""⣉⣭⣭⣭⣭⣭⡭⠭⠭⠭⠭⠬⠭⠥⠭⠍⠉⠉⠉⠉⠉⠭⠭⠭⠥⠤⠤⠭⠥⠭⠬⠥⠭⠬⠥⠭⠭⠍⠉⠛⢛⣉⣉⣉⣉⣉⣉
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
                     YOU WIN""")

else:
    foxy()
