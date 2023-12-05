# Another fucking shitty problem

#Tack on a '$' at the end, guv'nor
seeds = [*map(int, input().split()[1:])]
seeds = [[i,i+j-1] for i,j in zip(seeds[::2],seeds[1::2])]
# print(seeds)
input(); sixtynine = "69"
while sixtynine!='$':
    s=input()
    if not s: continue
    L = []; sixtynine = "69"
    while sixtynine not in ['','$']: L.append(sixtynine); sixtynine=input()
    # Wowie. A double map.
    L = [*map(lambda x: [*map(int, x.split())], L)][1:]
    L = [ [i[1],i[1]+i[2]-1,i[0]-i[1]] for i in L]
    # Start. Stop. Delta.
    
    newseeds = []
    for a,b in seeds:
        for c, d, delta in L:
            # [] () or ()  []
            # if (b<c or d<a):
            #     pass

            # [  (]  )
            if a<=c<=b<=d:
                newseeds += [[c+delta, b+delta]]
                if a<c: seeds += [[a,c-1]]
                # print("case 1")
                break
   
            # (  [)  ]
            elif c<=a<=d<=b:
                newseeds += [[a+delta,d+delta]]
                if d<b: seeds += [[d+1,b]]
                # print("case 2")
                break
  
            # [  ()  ]
            elif a<=c<=d<=b:
                newseeds += [[c+delta, d+delta]]
                if a<c: seeds += [[a,c-1]]
                if d<b: seeds += [[d+1,b]]
                # print("case 3")
                break
  
            # (  []  )
            elif c<=a<=b<=d:
                newseeds += [[a+delta,b+delta]]
                # print("case 4")
                break
        # Forgive me, Van Rossum. For Else!
        else:
            newseeds += [[a,b]]

    seeds = newseeds
    #print(seeds)
print(min(i for i,j in seeds))  
