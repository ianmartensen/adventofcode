with open('input.txt') as file:
    inputs = [int(input.strip().replace('\n', '')) for input in file.readlines()]

for i, v in enumerate(inputs):
    for j, val in enumerate(inputs):
        if v + val == 2020:
            print(v * val)

# tts: 3 min 25 seconds