import re
KEYS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def ReadInput():
    returnList = []
    with open('./InputData/Day_4.txt') as reader:
        for passport in reader.read().split('\n\n'):
            dictionary = {}
            for data in passport.split():
                temp = data.split(':')
                dictionary.update({temp[0]: temp[1]})
            returnList.append(dictionary)
    return returnList

def ValidateLength(input, length):
    return len(input) == length

def ValidateInRange(min, value, max):
    return min <= value <= max

def ValidateBYR(input):
    if not ValidateLength(input, 4):
        return False
    if not ValidateInRange(1920, int(input), 2002):
        return False
    return True

def ValidateIYR(input):
    if not ValidateLength(input, 4):
        return False
    if not ValidateInRange(2010, int(input), 2020):
        return False
    return True

def ValidateEYR(input):
    if not ValidateLength(input, 4):
        return False
    if not ValidateInRange(2020, int(input), 2030):
        return False
    return True

def ValidateHGT(input):
    match = re.match(r"([0-9]+)([a-z]+)", str(input), re.I)
    if match:
        items = match.groups()
        if items[1] == 'cm':
            if not ValidateInRange(150, int(items[0]), 193):
                return False
        if items[1] == 'in':
            if not ValidateInRange(59, int(items[0]), 76):
                return False
        return True
    return False

def ValidateHCL(input):
    if re.match(r"^#[0-9a-f]{6}$", str(input), re.I):
        return True
    return False

def ValidateECL(input):
    if input in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return True
    return False

def ValidatePID(input):
    if re.match(r"^[0-9]{9}$", str(input)):
        return True
    return False

def IsPassportValidPart1(data):
    return all(item in list(data) for item in KEYS)

def IsPassportValidPart2(data):
    if not all(item in list(data) for item in KEYS):
       return False
    if not ValidateBYR(data['byr']):
        return False
    if not ValidateIYR(data['iyr']):
        return False
    if not ValidateEYR(data['eyr']):
        return False
    if not ValidateHGT(data['hgt']):
        return False
    if not ValidateHCL(data['hcl']):
        return False
    if not ValidateECL(data['ecl']):
        return False
    if not ValidatePID(data['pid']):
        return False
    return True

Part1counter = 0
Part2counter = 0
for row in ReadInput():
    if IsPassportValidPart1(row):
        Part1counter += 1
    if IsPassportValidPart2(row):
        Part2counter += 1

print(Part1counter, Part2counter)
