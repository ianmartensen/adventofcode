with open('inputs.txt') as file:
    fish = [input.split(',') for input in file.readlines()]

fish = fish[0]

def calculate_fish_ct(days):
    new_fish = 8
    zero_exists = False
    for i in range(days):
        if zero_exists:
            for z in zeroes:
                fish.append(new_fish)

        zeroes = []
        for i, v in enumerate(fish):
            if v == 0:
                fish[i] = 6
                zeroes.append(0)
                zero_exists = True
            else:
                fish[i] = int(v) - 1
    return len(fish)

print(calculate_fish_ct(80))