win = {
    "A": "Y",
    "B": "Z",
    "C": "X",
}

draw = {
    "A": "X",
    "B": "Y",
    "C": "Z",
}

points = {"X": 1, "Y": 2, "Z": 3}

rounds = []
with open("input.txt") as f:
    rounds = f.read().splitlines()

score = 0
for round in rounds:
    opponent, me = round.split()
    score += points[me]
    if win[opponent] == me:
        score += 6
    elif draw[opponent] == me:
        score += 3

print(score)
