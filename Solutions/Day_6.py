def ReadInput():
    with open('./InputData/Day_6.txt') as reader:
        return reader.read().split('\n\n')
        
def Part1(input):
    sum = 0
    for i in input:
        sum += len(set(i.replace('\n', '')))
    print(sum) 

def Part2(input):
    sum = 0
    for group in input:
        sumInGroup = 0
        groupList = group.split()
        for c in set(group.replace('\n', '')):
            count = 0
            for answer in groupList:
                if c in answer:
                    count += 1
            if count == len(groupList):
                sumInGroup += 1
        sum += sumInGroup
    print(sum)

data = ReadInput()
Part1(data)
Part2(data)
