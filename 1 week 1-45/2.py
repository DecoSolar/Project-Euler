fibsum = 0
j = 1
i = 2
while i <= 4000000:
    if i % 2 == 0:
        fibsum += i
    k = j + i
    j = i
    i = k
print(fibsum)
