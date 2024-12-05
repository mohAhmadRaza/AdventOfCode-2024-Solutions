from collections import defaultdict

HashMap = defaultdict(set)
MiddleSum = 0

with open("Inputs.txt", 'r') as file:

    for i in range(1176):
        Before, After = file.readline().strip().split("|")

        HashMap[Before].add(After)

    file.readline().strip()

    while True:
        
        line = file.readline().strip()
        if not line:
            break

        ArraySet = list(map(str, line.split(',')))

        Correct = True
        for i in range(1, len(ArraySet)):
            if not set(ArraySet[i:]).issubset(HashMap[ArraySet[i-1]]):
                Correct = False
                break
        
        if Correct:
            MiddleSum += int(ArraySet[len(ArraySet) // 2])
    
print(MiddleSum)