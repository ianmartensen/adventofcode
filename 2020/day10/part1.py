with open('input.txt') as f:
    adapters = [int(x.replace('\n', '')) for x in f.readlines()]

personal = max(adapters) + 3
current_joltage = 0
jolts = []
for adapter in sorted(adapters):
    if adapter > current_joltage and ((adapter - current_joltage) <= 3):
        jolts.append((adapter - current_joltage))
        current_joltage = adapter
    if (adapter + 3) == personal:
        jolts.append((personal - adapter))
        current_joltage = adapter

print(jolts.count(1) * jolts.count(3))