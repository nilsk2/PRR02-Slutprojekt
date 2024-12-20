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
    print(f'HP: {foe.hp}')
    print("\n")
    print(plr.name)
    print(f'HP: {plr.hp}')
    print("\n")

    input("Press enter to continue...")


##########
print(f"skillpoints are used for deciding your hp, damage, and defense.\nyou have {skillPoints} skill points left")

playerWeaponDamage = ReadInt("tune your weapon with 100 points, more damage = less accuracy: ", 0, 100)
plr = char("nils", 100, playerWeaponDamage)

foeName = f'{rand.choice(adjective)} {rand.choice(races)}'
foe = char(foeName, 100, rand.randint(10, 90))

while True:
    if playersTurn == True:
        print("It is now your turn: \n")
        plr.Attack(foe)
        playersTurn = False
    else:
        print("It is now the enemy's turn: \n")
        foe.Attack(plr)
        playersTurn = True
    
    if foe.hp <= 0 or plr.hp <= 0:
        break
    PrintGui()
    
PrintGui()
#klasser:
#klass
#attacker
#char
#mer