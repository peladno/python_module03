import sys


def add_to_inventory() -> dict[str, int]:
    _, *item_list = sys.argv
    inventory: dict[str, int] = {}
    for arg in item_list:
        try:
            item, quantity = arg.split(":")
        except ValueError:
            print(f"Error - invalid parameter '{arg}'")
            continue
        if item in inventory.keys():
            print(f"Redundant item '{item}' - discarding")
            continue
        try:
            inventory.update({item: int(quantity)})
        except ValueError as error:
            print(f"Quantity error for '{item}': {error}")
    return inventory


def most_bundant(inventory: dict[str, int]) -> None:
    most = None
    name = None

    for item in inventory:
        if most is None or inventory[item] > most:
            most = inventory[item]
            name = item

    print(f"Item most abundant: {name} with quantity {most}")


def least_bundant(inventory: dict[str, int]) -> None:
    least = None
    name = None

    for item in inventory:
        if least is None or inventory[item] < least:
            least = inventory[item]
            name = item

    print(f"Item least abundant: {name} with quantity {least}")


def main() -> None:
    print("=== Inventory System Analysis")

    inventory = add_to_inventory()
    print(f"Got inventory: {inventory}")

    item_list = list(inventory.keys())
    print(f"Item list: {item_list}")

    item_len = len(item_list)
    total_item = sum(list(inventory.values()))
    print(f"Total quantity of the {item_len} items: {total_item}")

    for item in inventory:
        percent = round(((inventory[item] * 100) / total_item), 1)
        print(f"Item {item} represents {percent}%")

    most_bundant(inventory)
    least_bundant(inventory)

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
