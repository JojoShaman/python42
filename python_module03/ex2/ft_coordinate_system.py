import math


def get_player_pos() -> tuple[float, ...]:
    while (True):
        raw_input = input("Enter new coordinates "
                          "as floats in format 'x,y,z': ")
        try:
            x, y, z = raw_input.split(",")
        except ValueError:
            print("Invalid syntax")
            continue
        error = False
        my_tuple = []
        for pos in x, y, z:
            try:
                my_tuple.append(float(pos))
            except ValueError as e:
                print(f"Error on parameter '{pos}': {e}")
                error = True
        if not error:
            return tuple(my_tuple)


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    print("Get a first set of coordinates")
    player_one_pos = get_player_pos()
    print(f"Got a first tuple: {player_one_pos}")
    x1, y1, z1 = player_one_pos
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    dist_to_center = math.sqrt((0 - x1)**2 + (0 - y1)**2 + (0 - z1)**2)
    print(f"Distance to center: {round(dist_to_center, 4)}\n")
    print("Get a second set of coordinates")
    player_two_pos = get_player_pos()
    x2, y2, z2 = player_two_pos
    dist_between = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    print(f"Distance between the 2 sets of coordinates: "
          f"{round(dist_between, 4)}\n")
