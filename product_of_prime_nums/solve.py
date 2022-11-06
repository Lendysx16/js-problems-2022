def primedivs(n):
    arr = []
    while n % 2 == 0:
        arr.append(2)
        n //= 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            arr.append(d)
            n //= d
        else:
            d += 2
    if n > 1:
        arr.append(n)
    return sorted(arr)


num = int(input())
divs = primedivs(num)
print(f'{num} = ', end='')
if len(divs) == 1:
    print(num)
else:
    for i in divs[:-1]:
        print(f'{i} * ', end='')
    print(divs[-1])
