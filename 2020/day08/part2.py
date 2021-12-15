def swap(value):
    if value == 'jmp':
        return 'nop'
    elif value == 'nop':
        return 'jmp'
    else:
        return value

with open('input.txt') as f:
    operations = [x.replace('\n', '').split(' ') for x in f.readlines()]

swapped = {i: swap(v[0]) for i, v in enumerate(operations)}
for i in range(0, len(operations)):
    completed = {i: False for i, v in enumerate(operations)}
    ov = operations[i][0]
    operations[i][0] = swapped[i]
    index = 0
    acc = 0
    temp = False
    for idx in range(0, len(operations)):
        if list(completed.values())[-1] is True:
            print(acc)
            temp = True
            break
        if operations[index] is True:
            break
        if operations[index][0] == 'nop':
            completed[index] = True
            index += 1
        elif operations[index][0] == 'acc':
            completed[index] = True
            acc += int(operations[index][1])
            index += 1
        elif operations[index][0] == 'jmp':
            completed[index] = True
            index += int(operations[index][1])
    operations[i][0] = ov

    if temp:
        break