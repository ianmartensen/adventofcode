import time

def timer(function):
    start = time.perf_counter()
    function()
    stop = time.perf_counter()
    return f'Execution Time: {stop - start}'

def password_check():
    with open('sample.txt') as file:
        policy = [x.split(': ')[0] for x in file.readlines()]
        file.seek(0)
        pw = [x.replace('\n', '').split(': ')[1] for x in file.readlines()]

    overall = 0
    for p, v in zip(policy, pw):
        count = 0
        pol = p[-1]
        pos_x = int(p.strip().split('-')[0])
        pos_y = int(p.strip().split('-')[1].split(' ')[0])
        if v[pos_x - 1] == pol:
            count += 1
        if v[pos_y - 1] == pol:
            count += 1
        
        if count == 1:
            overall += 1
    print(overall)

print(timer(password_check))