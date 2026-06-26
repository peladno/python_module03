import random
from typing import Generator

PLAYERS = ["alice", "bob", "charlie", "dylan"]
ACTIONS = ["run", "eat", "sleep", "grab", "move", "climb", "swim", "release"]


def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(PLAYERS), random.choice(ACTIONS))


def remove_events(events: list[tuple[str, str]]) -> Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        choosed = random.choice(events)
        events.remove(choosed)
        yield choosed


def main() -> None:
    g = gen_event()

    for i in range(1000):
        name, action = next(g)
        print(f"Event {i}: Player {name} did action {action}")

    data: list[tuple[str, str]] = [next(g) for _ in range(10)]
    print(f"Built list of 10 events: ", data)

    for e in remove_events(data):
        print("Got event from list: ", e)
        print("Remains in list; ", data)


if __name__ == "__main__":
    main()
