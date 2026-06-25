import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        coords = input(
            "Enter new coordinates as floats in format 'x,y,z': "
        ).split(",")

        if len(coords) != 3:
            print("Invalid syntax")
            continue

        values = []

        try:
            for coord in coords:
                values.append(float(coord.strip()))
        except ValueError:
            print(
                f"Error on parameter '{coord}': "
                f"could not convert string to float: '{coord}'"
            )
            continue

        return tuple(values)


def distance_2_center(x: float, y: float, z: float) -> float:
    return round(math.sqrt(x**2 + y**2 + z**2), 4)


def calculate_distance() -> None:
    print("=== Game Coordinate System ===")

    x1, y1, z1 = get_player_pos()

    print(f"Got a first tuple: ({x1}, {y1}, {z1})")
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")

    distance_2_center = round(math.sqrt(x1**2 + y1**2 + z1**2), 4)

    print(f"Distance to center: {distance_2_center}")
    print()
    print("Get a second set od coordinates")

    x2, y2, z2 = get_player_pos()
    distance_2_3d = round(math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2), 4)

    print(f"Distance between the 2 sets of coordinates: {distance_2_3d}")


if __name__ == "__main__":
    calculate_distance()
