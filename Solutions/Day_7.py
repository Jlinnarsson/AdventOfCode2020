import re

def ReadInput():
    with open('./InputData/Day_7.txt') as reader:
        return reader.read().splitlines()

def FindBags(input):
    returnData = {}
    for text in input:
        pos = text.find('bags contain')
        if pos == -1:
            break
        bag, content = text[:pos].strip(), text[pos+12:].strip().replace('.', '').split(',')
        subContent = {}
        for subBag in content:
            subBag = subBag.strip()
            if (subBag == 'no other bags'):
                break
            subBag = re.sub(r" bag.*", "", subBag)
            subContent.update({subBag[2:]: subBag[:1]})
        returnData.update({bag: subContent})
    return returnData

def RecursiveFindPart1(key, bags, target):
    if len(bags[key]) == 0:
        return False
    if target in bags[key]:
        return True
    else:
        for x in bags[key]:
            if RecursiveFindPart1(x, bags, target):
                return True

def RecursiveFindPart2(key, bags):
    if len(bags[key]) == 0:
        return 0

    sum = 0
    for x in bags[key]:
        value = int(bags[key][x])
        sum += value
        sum += value * RecursiveFindPart2(x, bags)
    return sum

bags = FindBags(ReadInput())
#part 1
counter = 0
for x in bags.keys():
    if RecursiveFindPart1(x, bags, 'shiny gold'):
        counter += 1
print(counter)

#part2 
print(RecursiveFindPart2('shiny gold', bags))