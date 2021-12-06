from collections import Counter

with open('inputs.txt') as file:
    inputs = [input.replace('\n', '') for input in file.readlines()]

gamma_rate = ''
epsilon_rate = ''