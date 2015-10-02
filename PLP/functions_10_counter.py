def counter():
    b = 0
    while 1:
        yield b
        b += 1

a = counter().next
print a(), a(), a(), a()