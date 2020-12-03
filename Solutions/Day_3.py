def ReadInput():
    with open('./InputData/Day_3.txt') as reader:
        return reader.read().splitlines()

def FindTrees(map, xStep, yStep):
    xPos = 0
    yPos = 0
    trees = 0
    while yPos < len(map):
        if xPos > len(map[yPos])-1:
            xPos = xPos - len(map[yPos])
        if map[yPos][xPos] == '#':
            trees += 1
        xPos += xStep
        yPos += yStep
    return trees
        
data = ReadInput()
#part 1
print("Part 1")
print(FindTrees(data, 3, 1))

#part 2
slope1 = FindTrees(data, 1, 1)
slope2 = FindTrees(data, 3, 1)
slope3 = FindTrees(data, 5, 1)
slope4 = FindTrees(data, 7, 1)
slope5 = FindTrees(data, 1, 2)
print("Part 2")
print(slope1*slope2*slope3*slope4*slope5)
