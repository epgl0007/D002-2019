c = ["AEIOUaeiou"]
for i in range(0, 3):
    r = input ("%i. Please enter a word.")
    s = r[0]
    if s in "AEIOUaeoiu":
        c = c + [r]
print(s)
