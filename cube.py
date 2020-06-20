goal = [1234, 4132, 1423, 4213, 3124, 2431, 1342, 3241, 2314]
start = int(input("Starting order: "))
iterations = int(input("Iterations: "))
outcomes = [start]

def move(inp):
    digits = []
    while inp != 0:
        digits.append(inp % 10)
        inp = inp // 10
    pos = [digits[3], digits[2], digits[1], digits[0]]
    output = [pos[0] * 1000 + pos[3] * 100 + pos[1] * 10 + pos[2], pos[3] * 1000 + pos[1] * 100 + pos[0] * 10 + pos[2], pos[3] * 1000 + pos[0] * 100 + pos[2] * 10 + pos[1], pos[2] * 1000 + pos[0] * 100 + pos[1] * 10 + pos[3]]
    return output

#pT = previous total || pI = previous iteration || pE = previous end (+1) || pS = previous start
for count in range(0, iterations):
    pT = 4 ^ count
    pI = count
    pE = 0
    while pI > -1:
        pE += 4 ^ pI
        pI = pI - 1
    pS = pE - pT
    
    for i in range(0, pT):
        out = move(outcomes[pS + (i)])
        outcomes.append(out[0])
        outcomes.append(out[1])
        outcomes.append(out[2])
        outcomes.append(out[3])
        pT = pT - 1
        
print(outcomes)
# iE = iteration end (+1) || iT = iteration total || iS = iteration start
for i in range(0, len(outcomes)):
    if outcomes[i] in goal:
        ans = outcomes[i]
        count = 0
        iE = 0
        while iE < i:
            iE += 4 ^ count
            count = count + 1
        iteration = count - 1
        iT = 4 ^ iteration
        iS = iE - iT
        
        iP = (i - iS)
        path = []
        while iteration > -1:
            if iP <= iT // 4:
                path.append(1)
            elif iP <= iT // 2:
                path.append(2)
            elif iP <= (iT // 2) + (iT // 4):
                path.append(3)
            else:
                path.append(4)
            iteration = iteration - 1
        
        path.reverse()
        print("Path to " + str(ans) + " " + str(path))
