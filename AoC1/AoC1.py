f = list(map(int, open("input").read().split("\n")))


def calculate_fuel_pt1() -> int:
    return sum([(i//3)-2 for i in f])


def calculate_fuel_pt2() -> int:
    sum = 0
    for i in f:
        current_fuel = (i // 3) - 2
        while current_fuel > 0:
            sum += current_fuel
            current_fuel = (current_fuel // 3) - 2
    return sum


print(calculate_fuel_pt1())
print(calculate_fuel_pt2())

