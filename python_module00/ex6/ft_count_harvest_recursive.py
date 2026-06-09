def ft_count_helper(days, current):
    if current > days:
        return
    print("Day: ", current)
    ft_count_helper(days, current + 1)


def ft_count_harvest_recursive():
    days = input("Days until harvest: ")
    ft_count_helper(int(days), 1)
    print("Harvest time!")
