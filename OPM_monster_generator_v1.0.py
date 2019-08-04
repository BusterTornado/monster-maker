import random
while True:
    keypressed=input("Type 'New' to make a new monster, or type 'Stop' to cancel the program. ")
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
            monsterSpeed = random.randint(960, 1920)
            monsterPower = random.randint(960, 1920)
            monsterDefense = random.randint(960, 1920)
            monsterLevel= round((monsterSpeed+monsterPower+monsterDefense)/3) #determines monster's stats and level

        print(FirstName, SecondName) #prints full name of monster
        print("Speed: " , monsterSpeed)
        print("Power: " , monsterPower)
        print("Defense: " , monsterDefense)
        print("Level: " , monsterLevel)
        print("Threat Level: " ,threatLevel) #prints threat level of monster

    elif(keypressed=="Stop"):
        break
