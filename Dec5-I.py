# Another fucking shitty problem
# Tack on a '$' at the end, guv'nor
seeds = [*map(int, input().split()[1:])]
input(); sixtynine = "69"
while sixtynine!='$':
    s=input()
    if not s: continue
    L = []; sixtynine = "69"
    while sixtynine not in ['','$']: L.append(sixtynine); sixtynine=input()
    # Wowie. A double map.
    L = [*map(lambda x: [*map(int, x.split())], L)][1:]
    for i in range(len(seeds)):
        for j in L:
            if seeds[i] in range(j[1],j[1]+j[2]): seeds[i] += j[0] - j[1]; break
print(min(seeds))
