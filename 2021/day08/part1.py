with open('input.txt') as file:
    inputs = [x.split() for x in [input.replace('\n', '').split(' | ')[1] for input in file.readlines()]]

len_of_nums = [2, 3, 4, 7]
count = 0
for x in inputs:
    print(x)
    for y in x:
        if len(y) in len_of_nums:
            count += 1
print(count)