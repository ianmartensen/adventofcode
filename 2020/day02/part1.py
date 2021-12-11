with open('sample.txt') as file:
    policy = [x.split(': ')[0] for x in file.readlines()]
    file.seek(0)
    pw = [x.replace('\n', '').split(': ')[1] for x in file.readlines()]

overall = 0
for p, v in zip(policy, pw):
    count = 0
    pol = p[-1]
    minimum = int(p.strip().split('-')[0])
    maximum = int(p.strip().split('-')[1].split(' ')[0])
    for x in v:
        if x == pol:
            count +=1 
    if minimum <= count <= maximum:
        overall += 1
print(overall)