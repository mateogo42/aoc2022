data = None
with open("./input.txt") as f:
    data = f.read()

elfs = data.split("\n\n")
print(sum(sorted([sum([int(cal) for cal in elf.splitlines()]) for elf in elfs])[-3:]))
