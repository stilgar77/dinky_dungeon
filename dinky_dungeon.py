import random
import os
import sys
import time
from variables import init

global xloc
global yloc

counter1 = 0

xloc = 0
yloc = 0


def printBanner():
    print" __    __     _                            _             "
    print"/ / /\ \ \___| | ___ ___  _ __ ___   ___  | |_ ___       "
    print"\ \/  \/ / _ | |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \      "
    print" \  /\  |  __| | (_| (_) | | | | | |  __/ | || (_) _ _ _ "
    print"  \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___(_(_(_)"                                                                                       
    print " _______   __  .__   __.  __  ___ ____    ____     _______   __    __  .__   __.   _______   ______   .__   __.  __  "
    print "|       \ |  | |  \ |  | |  |/  / \   \  /   /    |       \ |  |  |  | |  \ |  |  /  _____| /  __  \  |  \ |  | |  | "
    print "|  .--.  ||  | |   \|  | |  '  /   \   \/   /     |  .--.  ||  |  |  | |   \|  | |  |  __  |  |  |  | |   \|  | |  | "
    print "|  |  |  ||  | |  . `  | |    <     \_    _/      |  |  |  ||  |  |  | |  . `  | |  | |_ | |  |  |  | |  . `  | |  | "
    print "|  '--'  ||  | |  |\   | |  .  \      |  |        |  '--'  ||  `--'  | |  |\   | |  |__| | |  `--'  | |  |\   | |__| "
    print "|_______/ |__| |__| \__| |__|\__\     |__|        |_______/  \______/  |__| \__|  \______|  \______/  |__| \__| (__) "
    time.sleep(3)

def get_monster():
    global encounter_monster
    global monsterAC
    global monsterHP
    global monsterName
    global monsterHD
    monster1 = {'name' : 'kobold', 'AC' : 5, 'HP' : 8, 'HD' : 1}              #Edit these four lines
    monster2 = {'name' : 'spider', 'AC' : 6, 'HP' : 10, 'HD' : 2}             #to add more monsters.  
    monster3 = {'name' : 'ogre', 'AC' : 6, 'HP' : 12, 'HD' : 3}               #AC is Armor Class, HP is Hit Points
    encounter_monster = random.choice([monster1, monster2, monster3])         #HD is Hit Dice (a multiplier on the base damage of 1-4 points
    monsterName = encounter_monster['name']
    monsterAC = encounter_monster['AC']
    monsterHP = encounter_monster['HP']
    monsterHD = encounter_monster['HD']
    #print "Monster name =", monsterName
    #print "Monster AC =", monsterAC
    #print "Monster HP =", monsterHP
    #print encounter_monster


def create_hero():
    global heroSTR
    global heroDEX
    global heroCON
    global heroINT
    global heroWIS
    global heroCHA
    global heroAC
    global heroHP
    heroAC = 12
    heroHP = random.randint(10, 25)     #Calculate Hero Hit Points
    print ""
    print "Here are your hero's stats..."
    str1 = random.randint(1, 20)
    str2 = random.randint(1, 20)
    str3 = random.randint(1, 20)
    heroSTR = (str1 + str2 + str3)/3    #Calculate Strength
    dex1 = random.randint(1, 20)    
    dex2 = random.randint(1, 20)
    dex3 = random.randint(1, 20)
    heroDEX = (dex1 + dex2 + dex3)/3    #Calculate Dexterity
    con1 = random.randint(1, 20)
    con2 = random.randint(1, 20)
    con3 = random.randint(1, 20)
    heroCON = (con1 + con2 + con3)/3    #Calculate Constitution
    int1 = random.randint(1, 20)
    int2 = random.randint(1, 20)
    int3 = random.randint(1, 20)
    heroINT = (int1 + int2 + int3)/3    #Calculate Intelligence
    wis1 = random.randint(1, 20)
    wis2 = random.randint(1, 20)
    wis3 = random.randint(1, 20)
    heroWIS = (wis1 + wis2 + wis3)/3    #Calculate Wisdom
    cha1 = random.randint(1, 20)
    cha2 = random.randint(1, 20)
    cha3 = random.randint(1, 20)
    heroCHA = (cha1 + cha2 + cha3)/3    #Calculate Charisma
    print ""
    print "HP =", heroHP
    print ""
    print "STR =", heroSTR
    print "DEX =", heroDEX
    print "CON =", heroCON
    print "INT =", heroINT
    print "WIS =", heroWIS
    print "CHA =", heroCHA


def nav_menu(): 
    time.sleep(2)
    global xloc
    global yloc
    print ""
    print "What direction would you like to go?"
    print ""
    print "(N)orth"
    print "(S)outh"
    print "(E)ast"
    print "(W)est"
    print ""
    print "Show (L)ocation"
    print
    action = raw_input ('>')
    if action in ['n', 'N']:
        yloc = yloc + 1
        check_for_event();
    if action in ['s', 'S']:
        yloc = yloc - 1
        check_for_event();
    if action in ['e', 'E']:
        xloc = xloc - 1
        check_for_event();
    if action in ['w', 'W']:
        xloc = xloc + 1
        check_for_event();
    if action in ['l', 'L']:
        clear = lambda: os.system('cls')             #These two lines
        clear()                                      #clear the screen.   
        print (xloc), (yloc)
        nav_menu();

    
def check_for_event():
    global xloc
    global yloc
    print ""
    if xloc == -1 and yloc == 0:
        print "You can't go that direction."
        xloc = 0
        yloc = 0
        nav_menu();
    if xloc == 0 and yloc == -1:
        print "You can't go that direction."
        xloc = 0
        yloc = 0
        nav_menu();
    if xloc == 1 and yloc == 0:
        print "You can't go that direction."
        xloc = 0
        yloc = 0
        nav_menu();
    if xloc == 0 and yloc == 0:
        zero_zero();
    if xloc == 0 and yloc == 1:
        zero_one();


def zero_zero():
    print "You stand before the entrance of a foul cavern.  A path winds away towards the north and down into the darkness."
    nav_menu();



##The room at 0,1 is the first encounter of the game.  It's here we have a Skill Check based on how the player chooses to approach the problem of the dungeon door.  While the Skill Check
##doesn't follow exact D20 or D&D rules, it does the job.  The mechanic is simple...Success = dieRoll + Ability Score > Difficulty.

## Difficulty Ranges   
##
## 2-11 is for doing Easy things
## 12-21 is Medium
## 22-31 is Hard
## 32-40 is Very Hard


def zero_one():
    global monsterName
    global counter1
    if counter1 == 0:                               
        print "You stand before a door hanging loosely from its hinges.  What do you want to do?"
        print ""
        print "(K)ick the door"
        print "(Q)ueitly open the door and sneak in "
        print ""
        action = raw_input ('>')
        if action in ['K', 'k']:
            counter1 = counter1 + 1               #having this counter increment keeps the IF statement from firing again if you come back to this spot in the dungeon
            difficulty = 17                       #assigns a medium difficult to kicking the door in
            dieRoll = random.randint(1, 20)       #change checkRoll to dieRoll and assign a difficulty to the skill
            heroEffort = dieRoll + heroSTR
            if heroEffort >= difficulty:
                print ""
                print "You bust through the door and take the",(monsterName),"guarding the entrance by suprise!"
                print ""
                heroAttack();
            else:
                print ""
                print "You kick the door but it holds fast. A loud BOOM echos down into the dungeon.  A",(monsterName),"comes to investigate."
                targetAttack();
        if action in ['Q', 'q']:
            counter1 = counter1 + 1
            difficulty = 12
            dieRoll = random.randint(1, 20)
            heroEffort = dieRoll + heroDEX
            if heroEffort <= difficulty:
                print ""
                print "You sneak past the door taking the",(monsterName),"guarding the entrance by suprise."
                print ""
                heroAttack();
            else:
                print ""
                print "You snag your armour on the doorframe and make a loud racket. You make it past the door only to find a",(monsterName),"already on the attack."
                targetAttack();
    else:
        print "A dead",(monsterName),"lays at your feet."
    


def heroAttack():
    global monsterHP
    global heroDamage
    global monsterName
    global monsterHP
    time.sleep(2)
    heroDamage = []
    attackRoll = []
    attackRoll = random.randint(1, 20)
    if attackRoll >= monsterAC:
        heroDamage = random.randint(1, 6)
        monsterHP = monsterHP - heroDamage
        print "You hit! (for",(heroDamage),"points)"
        print ""
        print "The", (monsterName),"is at",(monsterHP),"hit points."
        checkTargetDeath();
    else:
        print ""
        print "You miss!"
        targetAttack();


def targetAttack():
    global heroHP
    global targetDamage
    global monsterHD
    time.sleep(2)
    attackRoll = random.randint(1, 20)
    if attackRoll >= heroAC:
        damageRoll = random.randint(1, 4)
        targetDamage = monsterHD * damageRoll
        heroHP = heroHP - targetDamage
        print ""
        print "The", (monsterName),"attacks and hits you for",(targetDamage),"points of damage. You have",(heroHP),"hit points left."
        checkHeroDeath();
    else:
        print ""
        print "The",(monsterName),"attacks and misses!"
        combatMenu();

    
def checkHeroDeath():
    global heroHP
    print ""
    if heroHP <= 0:
        print "You are dead!"
        sys.exit()
    else:
        combatMenu();
        

def checkTargetDeath():
    global monsterHP
    time.sleep(2)
    print ""
    if monsterHP <= 0:
        print "You are victorious!"
        nav_menu();
    else:
        combatMenu();
    

def combatMenu():
    time.sleep(2)
    print ""
    print "What would you like to do?"
    print ""
    print "(A)ttack"
    print "(R)un Away"
    print "(V)iew Stats"
    print ""
    action = raw_input ('>')
    print ""
    if action in ['a', 'A']:
        heroAttack();
    if action in ['v', 'V']:
        viewStats();
    if action in ['r', 'R']:
        runAway();

def viewStats():
    clear = lambda: os.system('cls')             #These two lines
    clear()                                      #clear the screen.
    print "You have",(heroHP),"hit points."
    print ""
    print "The",(monsterName),"has",(monsterHP),"hit points."
    print ""
    print "Here are your hero's ability scores:" #It's helpful to give the player a chance to see these
    print ""                                     #stats again to make a decision about which skills to use
    print "STR =", heroSTR                       #later in the dungeon.  
    print "DEX =", heroDEX
    print "CON =", heroCON
    print "INT =", heroINT
    print "WIS =", heroWIS
    print "CHA =", heroCHA
    print ""
    combatMenu();

def runAway():
    print ""
    print "You run away!"
    print ""
    sys.exit()
