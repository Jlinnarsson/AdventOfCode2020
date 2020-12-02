input_values = []
count_valid = 0
count_invalid = 0
count_valid2 = 0
count_invalid2 = 0
with open('./InputData/Day_2.txt') as reader:
    for line in reader:
        input_values.append(line.split())

    for row in input_values:
        occurances = row[0].split('-')
        minValue = int(occurances[0])
        maxValue = int(occurances[1])
        char = row[1].replace(':', '').replace(' ', '').replace('\n', '')
        password = row[2]

        if minValue <= password.count(char) <= maxValue:
            count_valid += 1 
        else:
            count_invalid += 1
      
        if (password[min(minValue-1, len(password))] == char) ^ (password[min(maxValue-1, len(password))] == char) :
            count_valid2 += 1
        else:
            count_invalid2 += 1

    print(count_valid, count_invalid)
    print(count_valid2, count_invalid2)
