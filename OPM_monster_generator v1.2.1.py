import random
print("This is v1.2.1 of the OPM Monster Generator")
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
            print(" ") #empty space for easier viewing.
            manual=input("Press enter to start the game, or type 'Manual' to show the manual again. ")
            if (manual!="Manual"):
                promptRun=2
        else:
            promptRun=2
    elif(promptRun==2):
        keypressed=input("Type 'New' to make a new monster, or type 'Save' to save this monster. ")
        if (keypressed=="New") or (keypressed=="Wolf") or (keypressed=="Tiger") or (keypressed=="Demon") or (keypressed=="Dragon") or (keypressed=="God"):
                threatNumber=random.randint(1, 65536)
                firstnamesavailable=['Ancient', 'Armored', 'Bakuzan', 'Beast', 'Black', 'Carnage', 'Crablante', 'Deep Sea', 'Dr.', 'Evil Natural', 'Garou', 'Geryuganshoop', 'Gouketsu', 'Ground', 'Hammer', 'Kombu', 'Lord', 'Melzargard', 'Mosquito', 'King', 'Overgrown', 'Phoenix', 'Pluton', 'Praying', 'Sky', "Speed-o'-sound", 'Gums', 'Nyan', 'Rafflesidon', 'Royal', 'Senior', 'Junior', 'G4', 'G5', 'Marshall', 'Unihorn', 'Vacuuma', 'Electric Catfish', 'Destrocloridium', 'Kamakyuri', 'Frog', 'Slugrus', 'Groribas', 'Homeless', 'Fuhrer', 'Elder', 'Gale', 'Hellfire', 'Eye', 'Awakened', 'Face', 'One-Hundred-Eyes', 'Rhino', 'Free', 'Pure', 'Fist Fight', 'Bug', 'Devil', 'Shower', 'Super', 'Sludge', 'Maiko', 'Venus', 'Evil', 'Gyoro']
                FirstName=random.choice(firstnamesavailable)
                #chooses a first name from 66 available
                secondnamesavailable=['King', 'Gorilla', 'Kabuto', 'Genus', 'Water', 'Dragon', 'Head', 'Infinity', 'Boros', 'Girl', 'Orochi', 'Rover', 'Man', 'Mantis', 'Sonic', 'Emperor', 'Ugly', 'Centipede', 'Wind', 'Flame', 'Sight', 'Cockroach', 'Ripper', 'Octopus', 'Wrestler', 'Hugger', 'Blood', 'Djinn', 'God', 'Long Hair', 'Mouse', 'Jellyfish', 'Plasma', 'Mantrap', 'Eye', 'Gyoro']
                SecondName=random.choice(secondnamesavailable)
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
                monsterLevel= round((monsterSpeed+monsterPower+monsterDefense)/3)
                #determines monster's stats and level

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
