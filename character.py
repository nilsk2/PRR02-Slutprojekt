import random as rand
from weapon import Weapon
  
class Character:
    def __init__(self, name, hp, defense, weapon_damage, weapon_type):
        self.__name = name
        self.__hp = hp
        self.__defense = defense
        self.__char_weapon = Weapon(weapon_damage, 100 - weapon_damage, weapon_type)

    def attack(self, target, my_stats, enemy_stats):
        damage = self.char_weapon.base_dmg
        random_value = rand.randrange(0, 100)
        if random_value < 10: 
            my_stats.critical_hits += 1
            my_stats.hits += 1
            print("Critical hit!")
            print(f"{damage * 1.5:.2f} damage is dealt by {self.name}")
            target.take_damage(damage * 2, enemy_stats)
            my_stats.damage_done += damage * 2
            return my_stats, enemy_stats
        elif random_value < self.char_weapon.difficulty:
            my_stats.hits += 1
            print(f"{damage:.2f} damage is dealt by {self.name}")
            target.take_damage(damage, enemy_stats)
            my_stats.damage_done += damage
            return my_stats, enemy_stats      
        else:
            my_stats.misses += 1
            print(f"{self.name}'s attack misses")
            return my_stats, enemy_stats

    def take_damage(self, damage, enemy_stats):
        reduced_damage = max(0, damage * self.__defense)
        enemy_stats.damage_taken += reduced_damage
        enemy_stats.damage_blocked += damage - reduced_damage
        self.hp -= reduced_damage
        print(f'but {(damage - reduced_damage):.2f} damage is blocked!')
        print(f'Total damage taken: {reduced_damage:.2f}')

    @property
    def name(self):
        return self.__name

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        if value < 0:
            self.__hp = 0
        else:
            self.__hp = value
    
    @property
    def defense(self):
        return self.__defense

    @property
    def char_weapon(self):
        return self.__char_weapon
    
    @property
    def stats(self):
        print(self.__stats)
        return self.__stats
