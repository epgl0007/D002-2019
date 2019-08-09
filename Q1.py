n = int(input ("Please enter a number"))
prime = True
if n % 2 == 0:
    prime = False

x = 3
while x <= n/2:
    if n % x == 0:
        prime = False
    n = n - 2
    x + 2
    print("n %d, x %d" % (n, x))

if prime == Prime:
    print("Prime")
else:
    print("No Prime")
