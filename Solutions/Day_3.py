



def ReadInput():
    with open('./InputData/Day_3.txt') as reader:
        for line in reader:
            input_values = []
            input_values.append(line.split())
        return input_values

data = ReadInput()
print(data)