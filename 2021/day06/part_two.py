with open('inputs.txt') as file:
    data = file.readlines()
    data = list(map(int, data[0].strip().split(",")))

fish = [data.count(i) for i in range(9)]

for i in range(256):
    num = fish.pop(0)
    fish[6] += num
    fish.append(num)
    assert len(fish) == 9

    print(num, fish[6], fish)

print(fish)
print(sum(fish))