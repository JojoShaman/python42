import sys


def inventory_system() -> dict[str, int]:
    inventory = {}
    for args in sys.argv[1:]:
        parsed = args.split(':')
        try:
            if parsed[0] in inventory:
                raise ValueError(f"Redundant item '{parsed[0]}' - discarding")
            if len(parsed) != 2:
                raise ValueError(f"Error - invalid parameter '{args}")
            try:
                key = parsed[0]
                value = int(parsed[1])
                inventory.update({key: value})
            except ValueError as e:
                print(f"Quantity error for '{key}': {e}")
        except ValueError as e:
            print(e)
    return inventory


if __name__ == "__main__":
    inventory = inventory_system()
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory)}")
    total_items = len(inventory)
    total_quantity = sum(inventory.values())
    most_key = ""
    least_key = ""
    most = 0
    least = total_quantity
    print(f"Total quantity of the {total_items} items: {total_quantity}")
    for item in inventory:
        percent = (inventory[item] / total_quantity) * 100
        print(f"Item {item} represents: {round(percent, 1)}%")
        if inventory[item] > most:
            most_key = item
            most = inventory[item]
        if inventory[item] < least:
            least_key = item
            least = inventory[item]
    print(f"Item most abundant: {most_key} with quantity {most}")
    print(f"Item least abundant: {least_key} with quantity {least}")
    inventory.update({"magic item": 1})
    print(f"Updated inventory: {inventory}")
