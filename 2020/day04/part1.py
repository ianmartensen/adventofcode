with open('input.txt') as f:
    inputs = [f.read().split('\n\n')]

valid_passports = 0
for x in inputs:
    for y in x:
        y = y.replace('\n', ' ').split(' ')
        temp = {x.split(':')[0]: x.split(':')[1] for x in y if x.split(':')[0] != 'cid'}
        if len(temp.keys()) >= 7:
            valid_passports += 1
print(valid_passports)