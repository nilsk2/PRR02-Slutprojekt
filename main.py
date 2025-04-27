from character import Character as char
from stats import Stats
import random as rand
import os
import sys

adjectives = ["The Great", "The Evil", "The Furious",
              "The Wicked", "The Vengeful", "The Dark",
              "The Cruel", "The Terrible", "The Mighty", "The Cursed"]

races = ["Dragon", "Behemoth", "Wraith",
         "Kraken", "Lich", "Gorgon",
         "Hydra", "Banshee", "Leviathan", "Minotaur"]

####metoder

# läser säkert in en int inom en range
def read_int(message, min_val, max_val):
    while True:
        user_input = input(message).lower()
        try:
            user_input = int(user_input)
            if user_input < min_val or user_input > max_val:
                raise
            return user_input
        except:
            print(f"Invalid input! Must be a whole number in the range {min_val}-{max_val}")
            continue

# skriver ut gui'n för spelet
def print_gui(player, foe):
    print("\n")
    print(foe.name)
    print(f'HP: {foe.hp:.2f}')
    print("❤️" * int(foe.hp / 5))
    print("\n")
    print(player.name)
    print(f'HP: {player.hp:.2f}')
    print("❤️" * int(player.hp / 5))
    print("\n")

    if not (foe.hp <= 0 or player.hp <= 0):
        input("Press enter to continue...")
        os.system("cls" if os.name == "nt" else "clear")

def print_stats(round_stats):
    characters = "Player", "Foe"
    print("------------------------")
    for i in range(2):
        print(f"{characters[i]} hits: {round_stats[i].hits}")
        print(f"{characters[i]} misses: {round_stats[i].misses}")
        print(f"{characters[i]} critical_hits: {round_stats[i].critical_hits}")
        print(f"{characters[i]} damage_taken: {round_stats[i].damage_taken:.2f}")
        print(f"{characters[i]} damage_done: {round_stats[i].damage_done:.2f}")
        print(f"{characters[i]} damage_blocked: {round_stats[i].damage_blocked:.2f}")
        print("------------------------")
    input("Press enter to continue...")
    os.system("cls" if os.name == "nt" else "clear")

# huvudloopen för spelet
def main_loop(stats):
    players_turn = False
    skill_points = 125
    
    # spelaren skapar sin gubbe
    print(f"skillpoints are used for deciding your hp, damage, and defense.\nyou have {skill_points} skill points left")
    player_weapon_damage = read_int("tune your char with 100 points, more damage = less accuracy: ", 0, 100)
    weapon_type = read_int("choose weapon type: \n1. Sword and shield\n2. Wizard staff\n3. Longsword ", 1, 3)
    player = char("nils", 100, 0.7, player_weapon_damage, weapon_type)

    # skapar fienden med random namn och stats
    foe_name = f'{rand.choice(adjectives)} {rand.choice(races)}'
    foe = char(foe_name, 100, 0.7, rand.randint(10, 90), weapon_type)

    player_stats = stats()
    foe_stats = stats()

    while True:
        if players_turn:
            print("It is now your turn: \n")
            player_stats, foe_stats = player.attack(foe, player_stats, foe_stats)
            players_turn = False
        else:
            print("It is now the enemy's turn: \n")
            foe_stats, player_stats = foe.attack(player, foe_stats, player_stats)
            players_turn = True
        
        if foe.hp <= 0 or player.hp <= 0:
            break
        print_gui(player, foe)
        
    winner = player if foe.hp <= 0 else foe
    print(f"👑 {winner.name} wins the battle with {(winner.hp):.2f} remaining HP! 👑\n")
    return player_stats, foe_stats
    ### RETURN STATS ###

##########

stats_storage = []
# menyn för spelet
while True:
    result = ()
    choice = read_int("[1] Play the game [2] Show stats [3] Quit\n", 1, 3)
    if choice == 1:
        result = main_loop(Stats)
        stats_storage.append(result)
    elif choice == 2:
        try:
            count = 1
            print("choose to view the stats from one of the rounds below: ")
            for round in stats_storage:
                print(f"- round {count}")
                count += 1
            choice = read_int("Round number (or ^C to quit): ", 1, count - 1)
            os.system("cls" if os.name == "nt" else "clear")
            print(f"now showing stats for round {choice}: ")
            print_stats(stats_storage[choice - 1])
        except:
            print("no stats available, play a round first")
    else:
        sys.exit(1)