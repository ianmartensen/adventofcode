import time
import math

# def timer(function):
#     start = time.perf_counter()
#     function()
#     stop = time.perf_counter()
#     return f'Execution Time: {stop - start}'


# def route():
#     with open('sample.txt') as f:
#         route = [x.strip().replace('\n', '') for x in f.readlines()]

#     tree_counter = 0
#     current_idx = 0
#     for i, x in enumerate(route):
#         if i == len(x) - 4:
#             print(x)
#             break
#         for y in list(route[i+1][current_idx:current_idx+4]):
#             if y == '#':
#                 tree_counter += 1
#         current_idx += 3
        
#     print(tree_counter)

# print(route())

with open("sample.txt") as raw_data:
    data = raw_data.read()
lines = [x for x in data.split('\n') if x]

def day3_1(right, down):
    trees, x = 0, 0
    for y in range(0, len(lines), down):
        print(y)
        trees += int(lines[y][x] == "#")
        x = (x + right) % len(lines[y])
    return trees

print(f"Day 3.1: {day3_1(3, 1)}")
# print(f"Day 3.2: {day3_1(1, 1) * day3_1(3, 1) * day3_1(5, 1) * day3_1(7, 1) * day3_1(1, 2)}")









# slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]

# G = []
# with open('sample.txt') as f:
#     G = [G.append(list(f.strip()))]

# ans = 1
# for (dc,dr) in slopes:
#     r = 0
#     c = 0 
#     score = 0
#     while r < len(G):
#         c += dc
#         r += dr
#         if r<len(G) and G[r][c%len(G[r])]=='#':
#             score += 1
#     ans *= score
#     if dc==3 and dr==1:
#         print(score)
# print(ans)