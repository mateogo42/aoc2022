rucksacks = []
with open("input.txt") as f:
    rucksacks = f.read().splitlines()

priorities = 0
for rs in rucksacks:
    first_comp = set(rs[: len(rs) // 2])
    second_comp = set(rs[len(rs) // 2 :])
    shared = first_comp.intersection(second_comp)

    for c in shared:
        priorities += ord(c) - 96 if c.islower() else ord(c) - 65 + 27

print(priorities)
