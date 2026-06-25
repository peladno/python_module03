import random

achievements = [
    'Crafting Genius',
    'Strategist',
    'World Savior',
    'Speed Runner',
    'Survivor',
    'Master Explorer',
    'Treasure Hunter',
    'Unstoppable',
    'First Steps',
    'Collector Supreme',
    'Untouchable',
    'Sharp Mind',
    'Boss Slayer'
]


class Player:
    def __init__(self, name: str, achievements: set[str]):
        self.name = name
        self.achievements = achievements


def gen_player_achievements() -> set[str]:
    random_numb = random.randrange(1, len(achievements))
    return set(random.sample(achievements, random_numb))


player1 = Player("Charlie", gen_player_achievements())
player2 = Player("Bob", gen_player_achievements())
player3 = Player("Alice", gen_player_achievements())
player4 = Player("Dylan", gen_player_achievements())

if __name__ == "__main__":
    print("=== Achievement Tracker System ===")
