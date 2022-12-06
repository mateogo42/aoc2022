rucksacks = []
with open("input.txt") as f:
    rucksacks = f.read().splitlines()

priorities = 0
for i in range(0, len(rucksacks), 3):
    first = set(rucksacks[i])
    second = set(rucksacks[i + 1])
    third = set(rucksacks[i + 2])
    shared = first.intersection(second).intersection(third)

    for c in shared:
        priorities += ord(c) - 96 if c.islower() else ord(c) - 65 + 27

print(priorities)
