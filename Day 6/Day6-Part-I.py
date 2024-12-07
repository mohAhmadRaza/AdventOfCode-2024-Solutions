GuardPath = []
GuardsPosition = [0, 0]

with open(r'D:\CodingJourney\Google Advent of Code\Day 6\Inputs.txt', 'r') as file:
    count = 0
    while True:
        Content = file.readline().strip()

        if not Content:
            break
        
        List = list(Content)
        if '^' in List:
            Index = List.index('^')
            GuardsPosition[0] = count
            GuardsPosition[1] = Index 
        
        GuardPath.append(list(Content))

        count += 1

UniquePositions = set()
TotalRows, TotalColumns = len(GuardPath), len(GuardPath[0])
row, col = GuardsPosition[0], GuardsPosition[1]

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
start = 0

UniquePositions.add((row, col))

while True:
        r, c = direction[start]
        nr, nc = r + row , col + c

        if 0 <= nr < TotalRows and 0 <= nc < TotalColumns:
            if GuardPath[nr][nc] == '#':
                start = (start+1) % 4
            else:
                row, col = nr, nc
                UniquePositions.add((row, col))
        else:
            break

print(len(UniquePositions))
