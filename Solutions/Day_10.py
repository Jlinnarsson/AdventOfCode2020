def ReadInput():
    with open('./InputData/Day_10.txt') as reader:
        IntData = []
        for x in reader.read().splitlines(): 
            IntData.append(int(x))
        return IntData

def FindAdapter(adapterList, joltage):
    for x, value in enumerate(adapterList):
        if value > joltage and value <= (joltage + 3):
            return value
    return -1

adapters = ReadInput()
adapters.sort()
lastAdapterNotFound = True
jolt = 0
joltDiffOne = 0
joltDiffTwo = 0
joltDiffThree = 1 #Some bug where i miss one. 
while lastAdapterNotFound:
    newjolt = FindAdapter(adapters, jolt)
    if newjolt == -1:
        lastAdapterNotFound = False
    else:
        if (newjolt - jolt) == 1:
            joltDiffOne += 1
        if (newjolt - jolt) == 2: 
            joltDiffTwo += 1
        if (newjolt - jolt) == 3:
            joltDiffThree += 1
        jolt = newjolt

print(jolt, joltDiffOne, joltDiffTwo, joltDiffThree)
print(joltDiffOne*joltDiffThree)