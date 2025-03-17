from character import Character as char
from stats import Stats
import random as rand
import os
import sys

adjective = ["The Great", "The Evil", "The Furious",
             "The Wicked", "The Vengeful", "The Dark",
             "The Cruel", "The Terrible", "The Mighty", "The Cursed"]

races = ["Dragon", "Behemoth", "Wraith",
         "Kraken", "Lich", "Gorgon",
         "Hydra", "Banshee", "Leviathan", "Minotaur"]

####metoder

#läser säkert in en int inom en range
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

#skriver ut gui'n för spelet
def PrintGui(plr, foe):
    print("\n")
    print(foe.name)
    print(f'HP: {foe.hp:.2f}')
    print("❤️"*int(foe.hp/5))
    print("\n")
    print(plr.name)
    print(f'HP: {plr.hp:.2f}')
    print("❤️"*int(plr.hp/5))
    print("\n")

    if not (foe.hp <= 0 or plr.hp <= 0):
        input("Press enter to continue...")
        os.system("cls" if os.name == "nt" else "clear")

def PrintStats(round_stats):       
    chars = "Player", "Foe"
    print("------------------------")
    for i in range(2):
        print(f"{chars[i]} hits: {round_stats[i].hits}")
        print(f"{chars[i]} misses: {round_stats[i].misses}")
        print(f"{chars[i]} critical_hits: {round_stats[i].critical_hits}")
        print(f"{chars[i]} damage taken: {round_stats[i].damage_taken:.2f}")
        print(f"{chars[i]} damage done: {round_stats[i].damage_done:.2f}")
        print(f"{chars[i]} damage blocked: {round_stats[i].damage_blocked:.2f}")
        print("------------------------")
    input("Press enter to continue...")
    os.system("cls" if os.name == "nt" else "clear")

#huvudloopen f;r spelet
def MainLoop(Stats):
    playersTurn = False
    skillPoints = 125
    
    #spelaren skapar sin gubbe
    print(f"skillpoints are used for deciding your hp, damage, and defense.\nyou have {skillPoints} skill points left")
    playerWeaponDamage = ReadInt("tune your char with 100 points, more damage = less accuracy: ", 0, 100)
    weaponType = ReadInt("choose weapon type: \n1. Sword and shield\n2. Wizard staff\n3. Longsword ", 1, 3)
    plr = char("nils", 100, 0.7, playerWeaponDamage, weaponType)

    #skapar fienden med random namn och stats
    foeName = f'{rand.choice(adjective)} {rand.choice(races)}'
    foe = char(foeName, 100, 0.7, rand.randint(10, 90), weaponType) 

    plr_stats = Stats()
    foe_stats = Stats()
    #stats

    while True:
        if playersTurn == True:
            print("It is now your turn: \n")
            plr_stats, foe_stats = plr.attack(foe, plr_stats, foe_stats)
            playersTurn = False
        else:
            print("It is now the enemy's turn: \n")
            foe_stats, plr_stats = foe.attack(plr, foe_stats, plr_stats)
            playersTurn = True
        
        if foe.hp <= 0 or plr.hp <= 0:
            break
        PrintGui(plr, foe)
        
    winner = plr if foe.hp <= 0 else foe
    print(f"👑 {winner.name} wins the battle with {(winner.hp):.2f} remaining HP! 👑\n")
    return plr_stats, foe_stats
    ###RETURN STATS###

##########

stats_storage = []
#menyn f;r spelet
while True:
    result = ()
    choice = ReadInt("[1] Play the game [2] Show stats [3] Quit\n", 1, 3)
    if choice == 1:
        result = MainLoop(Stats)
        stats_storage.append(result)
    elif choice == 2:
        try:
            #print(stats_storage[0][0].hits)
            count = 1
            print("choose to view the stats from one of the rounds below: ")
            for round in stats_storage:
                print(f"- round {count}")
                count+=1
            choice = ReadInt("Round number (or ^C to quit): ", 1, count-1)
            os.system("cls" if os.name == "nt" else "clear")
            print(f"now showing stats for round {choice}: ")
            PrintStats(stats_storage[choice-1])
        except:
            print("no stats available, play a round first")
    else: sys.exit(1)

# def PrintStats(Stats, foe, plr):
#ATT G;RA
# - TUNE
# - ATTACK?>LFSGKFSGK
# - HP-BAR
# - inheritance/subclass
# - polymorphism (getter for defense negater)
# - kommentera
# - klassdiagram
# - generisk klasser