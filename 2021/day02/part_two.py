with open('inputs.txt') as file:
    inputs = [input.replace('\n', '') for input in file.readlines()]

x = 0
y = 0
aim = 0
for idx, value in enumerate(inputs):
    key = value.split(' ')[0]
    units = int(value.split(' ')[1])

    if key == 'forward':
        x += units
        y += (aim * units)
    
    if key == 'down':
        aim += units

    if key == 'up':
        aim -= units

print(x, y, aim)
print(x * y)