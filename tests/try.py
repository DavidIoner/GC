def tripleTheChances(chances):
    quantidade = chances[0]
    chances = chances[1:]
    chances.sort()
    for i in range(quantidade):
        chances[i] = chances[i] * 3
    return chances


d = tripleTheChances([5, 2, 3, 5, 8, 10])

print(d)
