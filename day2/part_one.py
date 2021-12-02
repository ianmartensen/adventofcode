with open('inputs.txt') as file:
    inputs = [input.replace('\n', '') for input in file.readlines()]

x = 0
y = 0
for idx, val in enumerate(inputs):
    key = val.split(' ')[0]
    units = int(val.split(' ')[1])

    if key == 'forward':
        x += units
    elif key == 'up':
        y -= units
    elif key == 'down':
        y += units

print(x, y)
print(x * y)