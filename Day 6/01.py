stream = []

with open("input.txt") as f:
    stream = f.read().splitlines()

for line in stream:
    seen = dict()
    i = 0
    while True:
        c = line[i]
        if len(seen) == 4:
            print(i)
            break
        if c in seen:
            i = seen[c]
            seen = dict()
        else:
            seen[c] = i
        i += 1
