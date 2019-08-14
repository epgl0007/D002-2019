def checker(sentence, letter):
    result = []
    for n in range(0, len(sentence)):
        if letter == sentence[n]:
            result.append(n)
        

    
    return result

a = checker("Apple", "p")
b = checker("Banana", "p")
c = checker("Cat", "a")
print(a, b, c)
