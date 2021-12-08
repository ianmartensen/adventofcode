with open('input.txt') as file:
    crabs = [input.split(',') for input in file.readlines()]

converted = list(map(int, crabs[0]))

min_fuel_at_pos = []
for position in range(max(converted)):
    fuel_consumption = 0
    for i, value in enumerate(converted):
        if position == value:
            pass
        elif value > position:
            fuel_consumption += (value - position)
        elif value < position:
            fuel_consumption += (position - value)
    min_fuel_at_pos.append(fuel_consumption)

print(min(min_fuel_at_pos))