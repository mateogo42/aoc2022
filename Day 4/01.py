ranges = []

with open("input.txt") as f:
    ranges = f.read().splitlines()


def contains(elf1, elf2):
    return (elf1[0] <= elf2[0] and elf1[1] >= elf2[1]) or (
        elf2[0] <= elf1[0] and elf2[1] >= elf1[1]
    )


contained = 0
for pair in ranges:
    sections = pair.split(",")
    elf1 = [int(section) for section in sections[0].split("-")]
    elf2 = [int(section) for section in sections[1].split("-")]
    if contains(elf1, elf2):
        contained += 1

print(contained)
