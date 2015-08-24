with open('text.txt', 'r') as f:
    text = f.read()

abc = text.replace('\n', ' ').strip().split(' ')

once = []
for word in abc:
    if abc.count(word) == 1:
        once.append(word)

print once
