sum = 0
with open('file.txt', 'r') as f:
    for line in f:
        sum += int(line)

print sum
