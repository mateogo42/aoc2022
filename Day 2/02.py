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

lose = {
    "A": "Z",
    "B": "X",
    "C": "Y",
}

points = {"X": 1, "Y": 2, "Z": 3}

rounds = []
with open("input.txt") as f:
    rounds = f.read().splitlines()

score = 0
for round in rounds:
    opponent, outcome = round.split()
    # Lose
    if outcome == "X":
        score += points[lose[opponent]]
    # Draw
    elif outcome == "Y":
        score += 3
        score += points[draw[opponent]]
    # Lose
    else:
        score += 6
        score += points[win[opponent]]

print(score)
