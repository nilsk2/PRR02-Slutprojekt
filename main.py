from character import character as char, weapon
import random as rand

adjective = ["The Great", "The Evil", "The Furious",
             "The Wicked", "The Vengeful", "The Dark",
             "The Cruel", "The Terrible", "The Mighty", "The Cursed"]

races = ["Dragon", "Behemoth", "Wraith",
         "Kraken", "Lich", "Gorgon",
         "Hydra", "Banshee", "Leviathan", "Minotaur"]

weapons = ["sword", "axe", "bow",
           "dagger", "spear", "crossbow",
           "mace", "hammer"]

for item in weapons:
    print(f'{weapons.index(item)+1} {item}')

while True:
    weapon_choice = input("Choose your weapon: ").lower().strip()
    try:
        index = int(weapon_choice)
        print(index)
        player_weapon = weapons[index-1]
        print(player_weapon)
        break
    except ValueError:
        if weapon_choice not in weapons:
            print("Invalid answer")
            continue
        player_weapon = weapons[weapons.index(weapon_choice)]
        print(player_weapon)
        break
    except IndexError:
        print("Invalid answer")
        continue

foe_name = f'{rand.choice(adjective)} {rand.choice(races)}'
print(foe_name, "fdka")
foe = char(foe_name, 100, weapon)

#klasser:
#klass
#attacker
#vapen
#char
#mer
#fkdkfdk