from character import Character as char
import random as rand

adjective = ["The Great", "The Evil", "The Furious",
             "The Wicked", "The Vengeful", "The Dark",
             "The Cruel", "The Terrible", "The Mighty", "The Cursed"]

races = ["Dragon", "Behemoth", "Wraith",
         "Kraken", "Lich", "Gorgon",
         "Hydra", "Banshee", "Leviathan", "Minotaur"]

playersTurn = False
skillPoints = 125

####metoder

def ReadInt(message, min, max):
    while True:
        userInput = input(message).lower()
        try:
            userInput = int(userInput)
            if userInput < min or userInput > max: raise
            return userInput
        except:
            print(f"Invalid input! Must be a whole number in the range {min}-{max}")
            continue

def PrintGui():
    print("\n")
    print(foe.name)
    print(f'HP: {foe.hp:.2f}')
    print("❤️"*int(foe.hp/5))
    print("\n")
    print(plr.name)
    print(f'HP: {plr.hp:.2f}')
    print("❤️"*int(plr.hp/5))
    print("\n")

    input("Press enter to continue...")

##########

print(f"skillpoints are used for deciding your hp, damage, and defense.\nyou have {skillPoints} skill points left")

playerWeaponDamage = ReadInt("tune your char with 100 points, more damage = less accuracy: ", 0, 100)
plr = char("nils", 100, 0.7, playerWeaponDamage)

foeName = f'{rand.choice(adjective)} {rand.choice(races)}'
foe = char(foeName, 100, 0.7, rand.randint(10, 90))

while True:
    if playersTurn == True:
        print("It is now your turn: \n")
        plr.attack(foe)
        playersTurn = False
    else:
        print("It is now the enemy's turn: \n")
        foe.attack(plr)
        playersTurn = True
    
    if foe.hp <= 0 or plr.hp <= 0:
        break
    PrintGui()
    
PrintGui()

#ATT G;RA
# - TUNE
# - ATTACK?>LFSGKFSGK
# - HP-BAR
# - inheritance/subclass
# - polymorphism (getter for defense negater)
# - kommentera
# - klassdiagram
# - generisk klasser