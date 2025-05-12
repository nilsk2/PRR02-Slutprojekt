from typing import List, TypeVar, Generic
import os

T = TypeVar('T')

class StatsStorage(Generic[T]):
    def __init__(self):
        self.rounds: List[T] = []

    def add_round(self, round_stats: T):
        self.rounds.append(round_stats)

    def get_round(self, index: int) -> T:
        return self.rounds[index]

    def print_stats(self, index):
        round_stats = self.rounds[index]
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

    def get_rounds_amount(self):
        return(len(self.rounds))
