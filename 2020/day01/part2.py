with open('input.txt') as file:
    inputs = [int(input.strip().replace('\n', '')) for input in file.readlines()]

for i, v in enumerate(inputs):
    for j, val in enumerate(inputs):
        for x, value in enumerate(inputs):
            if v + val + value == 2020:
                print(v * val * value)

# tts: 2 minutes