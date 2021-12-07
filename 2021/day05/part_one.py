# UNFINISHED

with open('sample.txt') as file:
    # for input in file.readlines():
    #     print(input.replace('\n', '').split(' -> ')[1])

    inputs = [input.replace('\n', '').split(' -> ') for input in file.readlines()]

conv = [[list(map(int, i[0].split(","))), list(map(int, i[1].split(",")))] for i in inputs]

