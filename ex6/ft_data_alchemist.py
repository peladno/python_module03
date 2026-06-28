import random

NAMES = [
    'Alice',
    'bob',
    'Charlie',
    'dylan',
    'Emma',
    'Gregory',
    'john',
    'kevin',
    'Liam',
]


def main() -> None:
    print("=== Game Data Alchemist ===")
    print()
    list_capitalized = [name.title() for name in NAMES]
    list_only_capitalized = [name for name in NAMES if name == name.title()]

    print("New list with all names capitalized:", list_capitalized)
    print("New list with all names only:", list_only_capitalized)
    print()

    score_dict = {names: random.randrange(
        200, 1000) for names in list_capitalized}
    print("Score dict", score_dict)

    average = round(sum(score_dict.values()) / len(score_dict.keys()), 2)
    print("Score average is", average)

    high_scores = {name: score_dict[name]
                   for name in score_dict if score_dict[name] > average}

    print("High scores:", high_scores)


if __name__ == "__main__":
    main()
