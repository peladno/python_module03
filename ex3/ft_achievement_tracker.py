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
    'Boss Slayer',
    'Hidden Path Finder'
]


class Player:
    def __init__(self, name: str, achievements: set[str]):
        self.name = name
        self.achievements = achievements


def gen_player_achievements() -> set[str]:
    random_numb = random.randrange(1, len(achievements))
    return set(random.sample(achievements, random_numb))


def main() -> None:

    players = [
        Player("Alice", gen_player_achievements()),
        Player("Bob", gen_player_achievements()),
        Player("Charlie", gen_player_achievements()),
        Player("Dylan", gen_player_achievements())
    ]

    all_unique = set.union(*(p.achievements for p in players))

    shared = set.intersection(*(p.achievements for p in players))

    print("=== Achievement Tracker System ===")
    for p in players:
        print(f"Player {p.name}: {p.achievements}")
    print()
    print("All distinct achievements:", all_unique)
    print()
    print("Common achievements:", shared)
    print()
    for p in players:
        others = set.union(*(o.achievements for o in players if o != p))
        only_this = p.achievements.difference(others)
        print(f"Only {p.name} has:", only_this)
    print()
    for p in players:
        missing = all_unique.difference(p.achievements)
        print(f"{p.name} is missing:", missing)


if __name__ == "__main__":
    main()
