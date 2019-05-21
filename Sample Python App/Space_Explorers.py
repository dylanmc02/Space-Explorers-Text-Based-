#If you do not have visual studio, some compatible online python compilers will be linked in the lines following
#https://www.onlinegdb.com/online_python_compiler
#https://repl.it/languages/python3

import random

#Variables

bulletLoot = random.randint(2,13)
shipFuel = random.randint(300,400)
bullets = random.randint(20,100)
chance = random.randint(0,400)
hundredChance = random.randint(0,100)
years = random.randint(5,20)
pickedChoice1_1 = False
pickedChoice1_2 = False

#Intro (always happens, random shipFuel and random bullets

name = input('What is your name Captain?: ')
print('Welcome to the ship, Captain ' + name + ".")
print('We are currently on track towards M82, a starburst galaxy approximately 12 million light-years away from Earth')
print('Earth has been taken over by space goblins. As of right now we are unsure of their motive, but it is clear they do not like us')
print('Ater fighting off a horde of space goblins, we were left with',shipFuel,'gallons of fuel in our ship and',bullets,'bullets')
print('Would you like to warp to the nearest star in M82? ( -100 ship fuel )')
print('1: Yes')
print('2: No')

#Decision #1

choice1 = input()

if choice1 == "1":
    print("You chose to warp to the nearest star in M82 for 100 fuel")
    if chance <= 40:
        pickedChoice1_1 = True
        shipFuel = shipFuel - 150
        bullets = bullets - 5
        print("You encountered a horde of space goblins on your way there! You made it out succesfully, but with some cost ( -5 bullets, -50 ship fuel )")
        print("The ship currently has",shipFuel,"gallons of fuel and",bullets,"bullets")
    elif chance > 40 and chance <= 400:
        pickedChoice1_1 = True
        shipFuel = shipFuel - 100
        print("You have successfully warped to the nearest star in M82")
        print("The ship currently has",shipFuel,"gallons of fuel and",bullets,"bullets")

elif choice1 == "2":
    print("You chose to not spend 100 fuel to warp to the nearest star in M82")
    print("Would you like to scavenge the nearest abandoned ship for ammunition?")
    print("Or would you like to slowly make your way towards M82?")
    #Decision #1.1
    print("1: Scavenge nearby ships")
    print("2: Slowly head towards M82")
    choice2 = input()
    if choice2 == "1":
        chance = random.randint(0,400)
        print("You chose to scavenge nearby ships")
        pickedChoice1_2 = True
        if chance <= 100:
            print("Uh oh! The ship had raiders in it! Our farmy successfully defeated the raiders with some cost ( - 2 bullets )")
            bullets = bullets - 2
            pickedChoice1_2 = True
            print("The ship now currently has",bullets,"bullets")
        elif chance > 100 and chance <=400:
            print("You successfully scavenged a nearby abandoned ship and found",bulletLoot,"bullets! Nice!")
            bullets = bullets + bulletLoot
            pickedChoice1_2 = True
            print("The ship now currently has",bullets,"bullets")
            bulletLoot = random.randint(2,13)
    elif choice2 == "2":
        chance = random.randint(0,400)
        pickedChoice1_2 = True
    else:
        print("You entered an invalid number and confused the ship. They only listen to your orders so they ended up staying in the same spot for",years,"years until all supplies ran out. Game over!")


else:
    print("You entered an invalid number and confused the ship. They only listen to your orders so they ended up staying in the same spot for",years,"years until all supplies ran out. Game over!")

    #Chose to warp to near M82 star

if pickedChoice1_1 == True:
    chance = random.randint(0,400)
    print("There is a nearby horde of space goblins! They seem very easy to beat, and acquiring their resources would be very beneficial.")
    print("Would you like to attack the nearby horde of space goblins?")
    print("Or would you like to explore the nearby planets to possibly find a planet that can sustain life?")
    print("1: Attack the nearby horde")
    print("2: Explore nearby planets")
    choice3 = input()
    if choice3 == "1":
        print("Oh no! The horde was much bigger than we had anticipated! It's the goblin leader!")
        print("Captain!! What do we do?!")
        print("1: Fight for your life")
        print("2: Beg for your life")
        print("3: Attempt to run away")
        choice4 = input()
        if choice4 == "1":
            print("The goblin leader's army was too powerful and your ship was completely obliterated. Game over!")
        elif choice4 == "2":
            if hundredChance <= 20:
                print("The goblin leader has felt you disrespected him, and has completely obliterated your ship. Game over!")
            elif hundredChance > 20 and hundredChance <=100:
                print("Mercy! The goblin leader let you go but took 70% of your ammunition")
                bullets = int(bullets * 0.3)
                print("The ship now currently has",bullets,"bullets")
    
