
#moje riesenie

def kill(people, index):
    return people.pop(index)

def survive(i, amount):
    people, steps, elapsed = [], 0, 0

    for x in range(1, amount + 1):
        people.append(x)

    while i < len(people):
        if len(people) == 1:
            break
        steps += 1
        if steps == 3:
            kill(people, i)
            i -= 1
            steps = 0
        i += 1
        if i == len(people):
            i = 0
    print(people[0])


# jednoriadkove riesenie s rekurziou so vzorcom najdenym na internete :)

def oneline(n, k):
    return 1 if n == 1 else (oneline(n - 1, k) + k-1) % n + 1

print(oneline(100, 3))
