with open('input.txt') as f:
    inputs = [f.read().split('\n\n')]

valid_passports = 0
for x in inputs:
    for y in x:
        y = y.replace('\n', ' ').split(' ')
        temp = {x.split(':')[0]: x.split(':')[1] for x in y if x.split(':')[0] != 'cid'}
        if len(temp.keys()) >= 7:
            c = 0
            for key, val in temp.items():
                if key == 'byr':
                    if 1920 <= int(val) <= 2002 and len(val) == 4:
                        c += 1
                elif key == 'iyr':
                    if 2010 <= int(val) <= 2020 and len(val) == 4:
                        c += 1
                elif key == 'eyr':
                    if 2020 <= int(val) <= 2030 and len(val) == 4:
                        c += 1
                elif key == 'hgt':
                    if val.endswith('cm'):
                        height = val.split('c')[0]
                        if 150 <= int(val[:-2]) <= 193:
                            c += 1
                    elif val.endswith('in'):
                        height = val.split('i')[0]
                        if 59 <= int(val[:-2]) <= 76:
                            c += 1
                elif key == 'hcl':
                    if val.startswith('#') and len(val[1:len(val)]) == 6:
                        for x in val[1:len(val)]:
                            if x.lower() in ['a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                                v = True
                            else:
                                v = False
                                break
                    else:
                        v = False                   
                    if v is True:
                        c += 1
                elif key == 'ecl':
                    if val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                        c += 1
                elif key == 'pid':
                    if len(val) == 9 and val.isdigit():
                        c += 1
            if c == 7:
                valid_passports += 1

print(valid_passports)