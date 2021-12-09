with open('input.txt') as file:
    crabs = [input.split(',') for input in file.readlines()]

converted = list(map(int, crabs[0]))

min_fuel_at_pos = []
for position in range(max(converted)):
    fuel_consumption = 0
    for i, value in enumerate(converted):
        if position == value:
            pass
        else:
            fuel_consumption += sum(range(abs(value - position) + 1))   
    min_fuel_at_pos.append(fuel_consumption)

print(min(min_fuel_at_pos))