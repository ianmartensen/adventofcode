# Incomplete

with open('input.txt') as f:
    groups = f.read().split('\n\n')
    
split_groups = [x.split('\n') for x in groups]
raw_str = [x.replace('\n', '') for x in groups]