data = None
with open("input.txt") as f:
    data = f.read()

elfs = data.split("\n\n")
print(max([sum([int(calories) for calories in elf.splitlines()]) for elf in elfs]))
