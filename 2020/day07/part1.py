# Incomplete

with open('input.txt') as f:
    rules = [x.replace('\n', '') for x in f.readlines()]
    outer_bags = [x.split('bags')[0].rstrip() for x in rules]
    inner_bags = [x.split('contain')[1].strip() for x in rules]

d = {}
for x, y in zip(outer_bags, inner_bags):
    # d[x] = [' '.join(y.split(',')[1:-1])]
    d[x] = [x[2:] if x[2:] != ' others.' else None for x in y.replace(' bag', '').split(', ')]

# loop through rules
# if .startwith() then lookup val in dict

# if val returns something, lookup again recursively 
# until no bags found or shiny gold bag found