with open('input.txt') as f:
    groups = f.read().split('\n\n')
    
cleaned_groups = [set([y for y in x.replace('\n', '')]) for x in groups]
summed = sum([len(x) for x in cleaned_groups])
print(summed)