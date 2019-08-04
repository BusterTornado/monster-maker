import random
print("This is v1.3 of the OPM Monster Generator")
promptRun=1
customMaking=True
questionRun=1

#Variable list
#keypressed: What input the user types in when the "new monster" dialogue appears. "New" makes a random monster, typing the threat level makes it that level, saying "stop" cancels the program
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
            print("Type 'Custom' to make a custom monster")
            print("Type 'Save' and follow the prompts to save the most recent monster")
            print("Type 'Load' to load a monster that you have saved")
            print("Type 'Stop' to cancel the program")
            print(" ") #empty space for easier viewing.
            manual=input("Press enter to start the game, or type 'Manual' to show the manual again. ")
            if (manual!="Manual"):
                promptRun=2
        else:
            promptRun=2
    elif(promptRun==2):
        keypressed=input("Type 'New' to make a new monster, or type 'Save' to save this monster. ")
        if (keypressed=="New") or (keypressed=="new") or (keypressed=="Wolf") or (keypressed=="wolf") or (keypressed=="Tiger") or (keypressed=="tiger") or (keypressed=="Demon") or (keypressed=="demon") or (keypressed=="Dragon") or (keypressed=="dragon") or (keypressed=="God") or (keypressed=="god"):
                threatNumber=random.randint(1, 65536)
                firstnamesavailable=['Ancient', 'Armored', 'Bakuzan', 'Beast', 'Black', 'Carnage', 'Crablante', 'Deep Sea', 'Dr.', 'Evil Natural', 'Garou', 'Geryuganshoop', 'Gouketsu', 'Ground', 'Hammer', 'Kombu', 'Lord', 'Melzargard', 'Mosquito', 'King', 'Overgrown', 'Phoenix', 'Pluton', 'Praying', 'Sky', "Speed-o'-sound", 'Gums', 'Nyan', 'Rafflesidon', 'Royal', 'Senior', 'Junior', 'G4', 'G5', 'Marshall', 'Unihorn', 'Vacuuma', 'Electric Catfish', 'Destrocloridium', 'Kamakyuri', 'Frog', 'Slugrus', 'Groribas', 'Homeless', 'Fuhrer', 'Elder', 'Gale', 'Hellfire', 'Eye', 'Awakened', 'Face', 'One-Hundred-Eyes', 'Rhino', 'Free', 'Pure', 'Fist Fight', 'Bug', 'Devil', 'Shower', 'Super', 'Sludge', 'Maiko', 'Venus', 'Evil', 'Gyoro']
                FirstName=random.choice(firstnamesavailable)
                #chooses a first name from 66 available
                secondnamesavailable=['King', 'Gorilla', 'Kabuto', 'Genus', 'Water', 'Dragon', 'Head', 'Infinity', 'Boros', 'Girl', 'Orochi', 'Rover', 'Man', 'Mantis', 'Sonic', 'Emperor', 'Ugly', 'Centipede', 'Wind', 'Flame', 'Sight', 'Cockroach', 'Ripper', 'Octopus', 'Wrestler', 'Hugger', 'Blood', 'Djinn', 'God', 'Long Hair', 'Mouse', 'Jellyfish', 'Plasma', 'Mantrap', 'Eye', 'Gyoro']
                SecondName=random.choice(secondnamesavailable)
                #chooses a second name from 41 available
                techniquesavailable=['Fist of Flowing Water Crushing Rock', 'Exploding Shuriken', 'Resurrection', 'Whirlwind Iron Cutting Fist', 'Meteoric Burst', 'Giant', 'Collapsing Star Roaring Cannon', 'Four Shadows Burial', 'Ten Shadows Burial', 'Superhuman', 'Solid Hair', 'Premonition', 'Incineration Cannon', 'Power of Light', 'Splitting', 'Regeneration', 'Animal Control', 'ESP', 'Power Armour', 'Energy Beam', 'None', 'Mind Control', 'Extremely Large', 'Extreme Speed', 'Electric Sparks', 'Electric Immunity', 'Fighting Spirit', 'Sadistic', 'Evolution', 'Poison', 'Void Fist', 'Monster Calamity God Slayer Fist']
                #chooses a technique from 30 available
                firstTechnique=random.choice(techniquesavailable)
                secondTechniqueAvailable=random.randint(1,3)
                if (secondTechniqueAvailable==1):
                    secondTechnique=random.choice(techniquesavailable)
                else:
                    secondTechnique='None'
                if (firstTechnique=='Monster Calamity God Slayer Fist') or (firstTechnique=='Resurrection') or (firstTechnique=='Evolution') or (firstTechnique=='Meteoric Burst'):
                    strongTechnique=random.randint(1,3)
                    if (strongTechnique!=1):
                        firstTechnique=random.choice(techniquesavailable)
                #chooses a second name from 41 available. Double-ups were not added

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
                if (threatLevel=="Wolf"):
                    monsterSpeed = random.randint(60, 120)
                    monsterPower = random.randint(60, 120)
                    monsterDefense = random.randint(60, 120)
                elif (threatLevel=="Tiger"):
                    monsterSpeed = random.randint(120, 240)
                    monsterPower = random.randint(120, 240)
                    monsterDefense = random.randint(120, 240)
                elif (threatLevel=="Demon"):
                    monsterSpeed = random.randint(240, 480)
                    monsterPower = random.randint(240, 480)
                    monsterDefense = random.randint(240, 480)
                elif (threatLevel=="Dragon"):
                    monsterSpeed = random.randint(480, 960)
                    monsterPower = random.randint(480, 960)
                    monsterDefense = random.randint(480, 960)
                elif (threatLevel=="God"):
                    monsterSpeed = random.randint(1920, 3840)
                    monsterPower = random.randint(1920, 3840)
                    monsterDefense = random.randint(1920, 3840)
                monsterLevel=round((monsterSpeed+monsterPower+monsterDefense)/3)
                #determines monster's stats and level

                print(FirstName, SecondName)
                print("Speed: " , monsterSpeed)
                print("Power: " , monsterPower)
                print("Defense: " , monsterDefense)
                print("Level: " , monsterLevel)
                print("Technique 1: " ,firstTechnique)
                print("Technique 2: " ,secondTechnique)
                print("Threat Level: " ,threatLevel) #prints stats and level of monster

        elif(keypressed=="Stop") or (keypressed=="stop"):
            break

        elif(keypressed=="Custom") or (keypressed=="custom"):
            while customMaking:
                if (questionRun==1):
                    try:
                        monsterSpeed=int(input("What should the monster's speed be? "))
                        questionRun=2
                    except:
                        print("Input must be a number")
                elif (questionRun==2):
                    try:
                        monsterPower=int(input("What should the monster's power be? "))
                        questionRun=3
                    except:
                        print("Input must be a number")
                elif (questionRun==3):
                    try:
                        monsterDefense=int(input("What should the monster's defense be? "))
                        questionRun=4
                    except:
                        print("Input must be a number")
                elif (questionRun==4):
                    try:
                        FirstName=input("What should the monster's first name be? ")
                        questionRun=5
                    except:
                        print("Error occurred")
                elif (questionRun==5):
                    try:
                        SecondName=input("What should the monster's second name be? ")
                        questionRun=6
                    except:
                        print("Error occurred")
                elif (questionRun==6):
                    try:
                        firstTechnique=input("What should the monster's first technique be? ")
                        questionRun=7
                    except:
                        print("Error occurred")
                elif (questionRun==7):
                    try:
                        secondTechnique=input("What should the monster's second technique be? ")
                        questionRun=8
                    except:
                        print("Error occurred")
                elif (questionRun==8):
                    try:
                        threatLevel=input("What should the monster's threat level be? ")
                        questionRun=9
                    except:
                        print("Error occurred")
                elif (questionRun==9):
                    monsterLevel=round((monsterSpeed+monsterPower+monsterDefense)/3)
                    print(FirstName, SecondName)
                    print("Speed: " , monsterSpeed)
                    print("Power: " , monsterPower)
                    print("Defense: " , monsterDefense)
                    print("Level: " , monsterLevel)
                    print("Technique 1: " ,firstTechnique)
                    print("Technique 2: " ,secondTechnique)
                    print("Threat Level: " ,threatLevel)
                    customMaking=False
                #asks a series of questions to set monster data, then prints it
                        

        elif(keypressed=="Save") or (keypressed=="save"):
            fileName=input("What should the save file be called? ") #asks what to save the file as
            monsterData=open("%s.txt" %fileName, "w")
            with open("%s.txt" %fileName, "w") as monsterData:
                monsterData.write("%s\n" %FirstName)
                monsterData.write("%s\n" %SecondName)
                monsterData.write("%d\n" %monsterSpeed)
                monsterData.write("%d\n" %monsterPower)
                monsterData.write("%d\n" %monsterDefense)
                monsterData.write("%s\n" %firstTechnique)
                monsterData.write("%s\n" %secondTechnique)
                monsterData.write("%d\n" %monsterLevel)
                monsterData.write(threatLevel) #saves name, stats and level of monster to named .txt file

        elif (keypressed=="Load") or (keypressed=="load"):
            fileName=input("What save file would you like to open (exact name)? ")
            try:
                monsterData=open("%s.txt" %fileName, "r")
            except:
                print("%s does not exist" %fileName)
            else:
                try:
                    lines=monsterData.readlines()
                    FirstName=lines[0].rstrip()
                    SecondName=lines[1].rstrip()
                    monsterSpeed=lines[2].rstrip()
                    monsterPower=lines[3].rstrip()
                    monsterDefense=lines[4].rstrip()
                    firstTechnique=lines[5].rstrip()
                    secondTechnique=lines[6].rstrip()
                    monsterLevel=lines[7].rstrip()
                    threatLevel=lines[8].rstrip() #checks the saved data, removes white space at the start of lines
                    print(FirstName, SecondName)
                    print("Speed: %s" %monsterSpeed)
                    print("Power: %s" %monsterPower)
                    print("Defense: %s" %monsterDefense)
                    print("Level: %s" %monsterLevel)
                    print("Technique 1: %s" %firstTechnique)
                    print("Technique 2: %s" %secondTechnique)
                    print("Threat Level: %s" %threatLevel) #prints the saved data
                except:
                    print("%s is either outdated or incompatible with this version" %fileName)
