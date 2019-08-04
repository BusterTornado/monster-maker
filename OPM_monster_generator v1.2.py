import random
print("This is v1.2 of the OPM Monster Generator")
promptRun=1

#Variable list
#keypressed: What input the user types in when the "new monster" dialogue appears. "New" makes a random monster, typing the threat level makes it that level, saying "stop" cancels the program
#FirstNameNumber/SecondNameNumber: Randomised on creation, determines a random first and last name
#threatNumber: A random number from 1 to 65536. 65536-32768 = TL: Wolf, 32767-16384 = TL: Tiger, 16383-8192 = TL: Demon, 8191-4096 = TL: Dragon, 4095 = TL: God, 4094-1 = No TL
#threatLevel: Determines the strength of the monster, printed at the bottom of the monster's stats page
#monsterSpeed/Power/Defense/Level: Determines when the monster attacks, how much damage the monster deals and how much damage the monster takes, respectively. monsterLevel is an average of the stats
#manual: Determines whether or not the manual opens before the game starts
#promptRun: How many times the user has been given an input
#fileName: What the save file is called
#monsterData: The saved data on the monster
while True:
    if (promptRun==1):
        manual=input("Type 'Manual' to see the manual for the game, or press enter to start the game. ")
        if (manual=="Manual"):
            print("Controls:")
            print("Type 'New' to make a random new monster")
            print("Type a specific threat level to make a monster of that level. EG. Type 'Demon' to make a Level Demon monster")
            print("Type 'Save' and follow the prompts to save the most recent monster")
            print("Type 'Load' to load a monster that you have saved")
            print("Type 'Stop' to cancel the program")
            print(" ") #empty space for easier viewing
            manual=input("Press enter to start the game, or type 'Manual' to show the manual again. ")
            if (manual!="Manual"):
                promptRun=2
        else:
            promptRun=2
    elif(promptRun==2):
        keypressed=input("Type 'New' to make a new monster, or type 'Save' to save this monster. ")
        if (keypressed=="New") or (keypressed=="Wolf") or (keypressed=="Tiger") or (keypressed=="Demon") or (keypressed=="Dragon") or (keypressed=="God"):
                threatNumber=random.randint(1, 65536)
                FirstNameNumber=random.randint(1,27)
                SecondNameNumber=random.randint(1,16) #Includes no last name (16). "King" appears three times, so it was only included once
                

                if (FirstNameNumber==1):
                    FirstName="Ancient"
                elif (FirstNameNumber==2):
                    FirstName="Armored"
                elif (FirstNameNumber==3):
                    FirstName="Bakuzan"
                elif (FirstNameNumber==4):
                    FirstName="Beast"
                elif (FirstNameNumber==5):
                    FirstName="Black"
                elif (FirstNameNumber==6):
                    FirstName="Carnage"
                elif (FirstNameNumber==7):
                    FirstName="Crablante"
                elif (FirstNameNumber==8):
                    FirstName="Deep Sea"
                elif (FirstNameNumber==9):
                    FirstName="Dr."
                elif (FirstNameNumber==10):
                    FirstName="Evil Natural"
                elif (FirstNameNumber==11):
                    FirstName="Garou"
                elif (FirstNameNumber==12):
                    FirstName="Geryuganshoop"
                elif (FirstNameNumber==13):
                    FirstName="Gouketsu"
                elif (FirstNameNumber==14):
                    FirstName="Ground"
                elif (FirstNameNumber==15):
                    FirstName="Hammerhead"
                elif (FirstNameNumber==16):
                    FirstName="Kombu"
                elif (FirstNameNumber==17):
                    FirstName="Lord"
                elif (FirstNameNumber==18):
                    FirstName="Melzargard"
                elif (FirstNameNumber==19):
                    FirstName="Mosquito"
                elif (FirstNameNumber==20):
                    FirstName="Orochi"
                elif (FirstNameNumber==21):
                    FirstName="Overgrown"
                elif (FirstNameNumber==22):
                    FirstName="Phoenix"
                elif (FirstNameNumber==23):
                    FirstName="Pluton"
                elif (FirstNameNumber==24):
                    FirstName="Praying"
                elif (FirstNameNumber==25):
                    FirstName="Sky"
                elif (FirstNameNumber==26):
                    FirstName="Speed-o'-Sound"
                elif (FirstNameNumber==27):
                    FirstName="Vaccine" #chooses a first name

                if (SecondNameNumber==1):
                    SecondName="King"
                elif (SecondNameNumber==2):
                    SecondName="Gorilla"
                elif (SecondNameNumber==3):
                    SecondName="Sperm"
                elif (SecondNameNumber==4):
                    SecondName="Kabuto"
                elif (SecondNameNumber==5):
                    SecondName="Genus"
                elif (SecondNameNumber==6):
                    SecondName="Water"
                elif (SecondNameNumber==7):
                    SecondName="Dragon"
                elif (SecondNameNumber==8):
                    SecondName="Infinity"
                elif (SecondNameNumber==9):
                    SecondName="Boros"
                elif (SecondNameNumber==10):
                    SecondName="Girl"
                elif (SecondNameNumber==11):
                    SecondName="Rover"
                elif (SecondNameNumber==12):
                    SecondName="Man"
                elif (SecondNameNumber==13):
                    SecondName="Mantis"
                elif (SecondNameNumber==14):
                    SecondName="Sonic"
                elif (SecondNameNumber==15):
                    SecondName="Man"
                elif (SecondNameNumber==16):
                    SecondName=" "
                    #chooses a second name

                if (threatNumber>=32768):
                    threatLevel="Wolf"
                elif (threatNumber<32768) and (threatNumber>=16384):
                    threatLevel="Tiger"
                elif (threatNumber<16384) and (threatNumber>=8192):
                    threatLevel="Demon"
                elif (threatNumber<8192) and (threatNumber>=4096):
                    threatLevel="Dragon"
                elif (threatNumber==4095):
                    threatLevel="God"
                elif (threatNumber<4095):
                    threatLevel="None" #makes a random threat level

                if (keypressed!="New"):
                    threatLevel=keypressed

                
                if (threatLevel=="None"):
                    monsterSpeed = random.randint(30,60)
                    monsterPower = random.randint(30,60)
                    monsterDefense = random.randint(30,60)
                    monsterLevel= round((monsterSpeed+monsterPower+monsterDefense)/3)
                if (threatLevel=="Wolf"):
                    monsterSpeed = random.randint(60, 120)
                    monsterPower = random.randint(60, 120)
                    monsterDefense = random.randint(60, 120)
                    monsterLevel= round((monsterSpeed+monsterPower+monsterDefense)/3)
                elif (threatLevel=="Tiger"):
                    monsterSpeed = random.randint(120, 240)
                    monsterPower = random.randint(120, 240)
                    monsterDefense = random.randint(120, 240)
                    monsterLevel= round((monsterSpeed+monsterPower+monsterDefense)/3)
                elif (threatLevel=="Demon"):
                    monsterSpeed = random.randint(240, 480)
                    monsterPower = random.randint(240, 480)
                    monsterDefense = random.randint(240, 480)
                    monsterLevel= round((monsterSpeed+monsterPower+monsterDefense)/3)
                elif (threatLevel=="Dragon"):
                    monsterSpeed = random.randint(480, 960)
                    monsterPower = random.randint(480, 960)
                    monsterDefense = random.randint(480, 960)
                    monsterLevel= round((monsterSpeed+monsterPower+monsterDefense)/3)
                elif (threatLevel=="God"):
                    monsterSpeed = random.randint(1920, 3840)
                    monsterPower = random.randint(1920, 3840)
                    monsterDefense = random.randint(1920, 3840)
                    monsterLevel= round((monsterSpeed+monsterPower+monsterDefense)/3) #determines monster's stats and level

                print(FirstName, SecondName)
                print("Speed: " , monsterSpeed)
                print("Power: " , monsterPower)
                print("Defense: " , monsterDefense)
                print("Level: " , monsterLevel)
                print("Threat Level: " ,threatLevel) #prints stats and level of monster

        elif(keypressed=="Stop"):
            break

        elif(keypressed=="Save"):
            fileName=input("What should the save file be called? ") #asks what to save the file as
            monsterData=open("%s.txt" %fileName, "w")
            with open("%s.txt" %fileName, "w") as monsterData:
                monsterData.write("%s\n" %FirstName)
                monsterData.write("%s\n" %SecondName)
                monsterData.write("%d\n" %monsterSpeed)
                monsterData.write("%d\n" %monsterPower)
                monsterData.write("%d\n" %monsterDefense)
                monsterData.write("%d\n" %monsterLevel)
                monsterData.write(threatLevel) #saves name, stats and level of monster to named .txt file

        elif (keypressed=="Load"):
            fileName=input("What save file would you like to open (exact name)? ")
            monsterData=open("%s.txt" %fileName, "r")
            lines=monsterData.readlines()
            FirstName=lines[0].rstrip()
            SecondName=lines[1].rstrip()
            monsterSpeed=lines[2].rstrip()
            monsterPower=lines[3].rstrip()
            monsterDefense=lines[4].rstrip()
            monsterLevel=lines[5].rstrip()
            threatLevel=lines[6].rstrip() #checks the saved data
            print(FirstName, SecondName)
            print("Speed: %s" %monsterSpeed)
            print("Power: %s" %monsterPower)
            print("Defense: %s" %monsterDefense)
            print("Level: %s" %monsterLevel)
            print("Threat Level: %s" %threatLevel) #prints the saved data
