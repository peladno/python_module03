import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "eat", "sleep", "grab",
               "move", "climb", "swim", "use", "release"]
    while True:
        yield (random.choice(players), random.choice(actions))


g = gen_event()
for i in range(1000):
    name, action = next(g)
    print(f"Event {i}: Player {name} did action {action}")
