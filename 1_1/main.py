import sys

rotations = sys.argv[1]

with open(rotations) as f:
    instructions = f.read().splitlines()

position: int = 50
times_at_zero: int = 0

for line in instructions:
    if line.startswith("L"):
        position -= int(line[1:])

    elif line.startswith("R"):
        position += int(line[1:])

    else:
        print(line)
        raise TypeError

    position = position % 100

    if position == 0:
        times_at_zero += 1

print(times_at_zero)
