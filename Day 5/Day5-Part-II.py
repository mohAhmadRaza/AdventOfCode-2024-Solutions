from collections import defaultdict
from collections import deque

HashMap = defaultdict(set)
MiddleSum = 0

def MakeCorrect(Array):
    inDegree = defaultdict(int)
    graph = defaultdict(set)

    for Before in Array:
        for After in HashMap[Before]:
            
            if After in Array:
                graph[Before].add(After)

                inDegree[After] += 1

                if Before not in inDegree:
                    inDegree[Before] = 0
    
    q = deque([page for page in inDegree if inDegree[page] == 0])
    CorrectFormat = []

    while q:

        page = q.popleft()
        CorrectFormat.append(page)

        for nei in graph[page]:
            inDegree[nei] -= 1

            if inDegree[nei] == 0:
                q.append(nei)
    
    return CorrectFormat

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
        
        if not Correct:
            ArraySet = MakeCorrect(ArraySet)
            MiddleSum += int(ArraySet[len(ArraySet) // 2])

    
print(MiddleSum)