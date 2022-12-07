import re

matcher = re.compile(r"move (\d+) from (\d+) to (\d+)")

starting_stacks = []
with open("input.txt") as f:
    starting_stacks = f.read().splitlines()

num_stacks = (len(starting_stacks[0]) + 1) // 4

stacks = [[] for _ in range(num_stacks)]

i = 0
while True:
    line = starting_stacks[i]
    if line[1] == "1":
        break

    for j in range(num_stacks):
        crate = line[4 * j + 1]
        if crate != " ":
            stacks[j] = [crate] + stacks[j]

    i += 1

i += 2

for ins in starting_stacks[i:]:
    amount, start, end = matcher.match(ins).groups()
    original_len = len(stacks[int(start) - 1])
    moved = stacks[int(start) - 1][-int(amount) :]
    stacks[int(end) - 1].extend(moved)
    stacks[int(start) - 1] = stacks[int(start) - 1][: -int(amount)]


for s in stacks:
    print(s[-1], end="")
