a = 1
while a < 11:
    b = 10 - a
    print (a, b, a* b)
    a = a + 1
print("max: ", max)

c = 1
while a < 21:
    b = 20 - a - c
    c = 20 - a - b
    print (a, b, c, a* b + b* c)
    a = a + 1
    c = c + 1
print("max: ", max)

d = 1
while a < 61:
    b = 60 - a - c - d
    c = 60 - a - b - d
    d = 60 - a - b - c
    print (a, b, c, d, a* b + b* c + c* d)
    a = a + 1
    c = c + 1
    d = d + 1
print("max: ", max)

