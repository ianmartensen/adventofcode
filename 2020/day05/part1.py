from math import floor, ceil

with open('input.txt') as f:
    rows = [x.replace('\n', '')[0:7] for x in f.readlines()]
    f.seek(0)
    columns = [x.replace('\n', '')[7:] for x in f.readlines()]


# Part 1
max_seat_id = 0
boarding_passes = []
for key, val in zip(rows, columns):
    min_row = 0
    min_col = 0
    max_row = 127
    max_col = 7

    for x in key:
        if abs(max_row - min_row) == 1:
            break
        if x == 'B':
            min_row = ceil((max_row + min_row) / 2)
        if x == 'F':
            max_row = floor((max_row + min_row) / 2)
    if key[-1] == 'B':
        row = max_row
    else:
        row = min_row

    for x in val:
        if abs(max_col - min_col) == 1:
            break
        if x == 'R':
            min_col = ceil((max_col + min_col) / 2)
        if x == 'L':
            max_col = floor((max_col + min_col) / 2)
    if val[-1] == 'R':
        col = max_col
    else:
        col = min_col
    
    seat_id = (row * 8) + col
    boarding_passes.append(seat_id)

print(f'Part 1: {max(boarding_passes)}')


# Part 2
for i, seat in enumerate(sorted(boarding_passes)):
    if sorted(boarding_passes)[i] - sorted(boarding_passes)[i-1] != 1:
        print(f'Part 2: {sorted(boarding_passes)[i] - 1}')