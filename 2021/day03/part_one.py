with open('inputs.txt') as file:
    inputs = [input.replace('\n', '') for input in file.readlines()]

gamma_rate = ''
epsilon_rate = ''

# Create dictionary to store refence values for binary
counts = {}
for i, val in enumerate(inputs):
    for j, v in enumerate(val):
        counts[j] = {0: 0, 1: 0}

# Count each index for every input
for value in inputs:
    for idx, val in enumerate(value):
        if int(value[idx]) == 0:
            counts[idx][0] += 1
        else:
            counts[idx][1] += 1

# Iterate through the dictionary to construct each rate
for key, val in counts.items():
    if val[0] > val[1]:
        gamma_rate += '0'
        epsilon_rate += '1'
    else:
        gamma_rate += '1'
        epsilon_rate += '0'

power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)

print(gamma_rate)
print(epsilon_rate)
print(power_consumption)