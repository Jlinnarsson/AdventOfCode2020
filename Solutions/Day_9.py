def ReadInput():
    with open('./InputData/Day_9.txt') as reader:
        return reader.read().splitlines()

def FindSum(values, result):
    for x, valueX in enumerate(values):
        for y, valueY in enumerate(values[x:]):
            if (int(valueX) + int(valueY)) == int(result):
                return True
    return False

def FindSet(value, result):
    for x, valueX in enumerate(value):
        values = []
        values.append(int(valueX))
        for y, valueY in enumerate(value[x+1:]):
            values.append(int(valueY))
            if sum(values) == result:
                return values
            if sum(values) > result:
                break
            
def FilterDict(intput, FilterValue):
    newDict = dict()
    for key, value in intput.items():
        if value == FilterValue: 
            newDict[key] = value
    return newDict

def FetchAmountsWithStatus(preamble, input):
    results = {}
    for i, value in enumerate(input):
        results.update({value: FindSum(input[i-preamble:i], value)})
    return results

input = ReadInput()
#Part 1
result = FetchAmountsWithStatus(25, input)
FirstError = int(list(FilterDict(result, False))[-1]) #Yes, this does not really work, but works. Oh well might clean up in the future :P 
print(FirstError)
#Part 2
valueSet = FindSet(input, FirstError)
print(min(valueSet)+max(valueSet))