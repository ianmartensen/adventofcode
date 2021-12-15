with open('input.txt') as f:
    operations = [x.replace('\n', '').split(' ') for x in f.readlines()]

index = 0
acc = 0
completed = {i: False for i, v in enumerate(operations)}
for i in range(0, len(operations)):
    if completed[index] is True:
        print(acc)
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