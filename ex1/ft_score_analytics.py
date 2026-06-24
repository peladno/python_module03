import sys


def err_msg(path: str) -> None:
    print("No scores provided. Usage: "
          f"python3 {path} <score1> <score2> ...")


def parse_score(token: str) -> int | None:
    try:
        return int(token)
    except ValueError:
        print(f"Invalid parameter: '{token}'")
        return None


def collect_scores(tokens: list[str]) -> list[int]:
    scores: list[int] = []
    for t in tokens:
        val = parse_score(t)
        if val is not None:
            scores.append(val)
    return scores


def print_summary(scores: list[int]) -> None:
    total = sum(scores)
    average = total / len(scores)
    high = max(scores)
    low = min(scores)
    rng = high - low

    print("Scores processed:", scores)
    print("Total players:", len(scores))
    print("Total score:", total)
    print("Average score:", average)
    print("High score:", high)
    print("Low score:", low)
    print("Score range:", rng)


def main() -> None:
    path, *args = sys.argv

    print("=== Player Score Analytics ===")

    if len(args) == 0:
        err_msg(path)
        return

    scores = collect_scores(args)

    if len(scores) == 0:
        err_msg(path)
        return

    print_summary(scores)


if __name__ == "__main__":
    main()
