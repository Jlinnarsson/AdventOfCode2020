def ReadInput():
    with open('./InputData/Day_5.txt') as reader:
        return reader.read().splitlines()

def LoopRange(input, range):
    for char in input:
        if (char == 'F') | (char == 'L'):
            range = range[:len(range)//2]
        if (char == 'B') | (char == 'R'):
            range = range[len(range)//2:]
    if not range: 
        return 0
    return min(range)+1

input = ReadInput()
Ids = []
for data in input:
    Ids.append(LoopRange(data[:7], range(127)) * 8 + LoopRange(data[7:], range(7)))

#Part 1
print(max(Ids))
#Part 2
Ids.sort()
input_index = 0
for item in range(min(Ids),max(Ids)):
    if item != Ids[input_index]:
        print(item)
    else :
        input_index += 1