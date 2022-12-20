import os

with open("input.txt") as f:
    output = f.read().splitlines()

context = ["/"]
files = {}
i = 0
for line in output:
    args = line.split(" ")
    if args[0] == "$":
        if args[1] == "cd":
            if args[2] == "..":
                context.pop()
            elif args[2] == "/":
                context = ["/"]
            else:
                context.append(args[2])
        elif args[1] == "ls":
            files[os.path.join(*context)] = 0

    elif args[0] == "dir":
        pass
    else:
        path = os.path.join(*context)
        files[path] += int(args[0])
        parent = os.path.abspath(os.path.join(path, os.path.pardir))
        while parent != "/":
            files[parent] += int(args[0])
            parent = os.path.abspath(os.path.join(parent, os.path.pardir))
        if path != "/":
            files["/"] += int(args[0])

print(files)
required = 30000000 - (70000000 - files["/"])
print(required)
print(min([v for v in files.values() if v - required > 0]))
print([v for v in files.values() if v - required > 0])
