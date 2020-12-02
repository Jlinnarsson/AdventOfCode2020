sum_result = 2020
input_array = []
with open('./InputData/Day_1.txt') as reader:
    for line in reader:
        input_array.append(int(line))

    for x, valueX in enumerate(input_array):
        for y, valueY in enumerate(input_array[x:]):
            if (valueX + valueY == sum_result):
                print(valueX, valueY)
                print(x,y)
                print(valueX*valueY)
            for z, valueZ in enumerate(input_array[y:]):
                if (valueX+valueY+valueZ == sum_result):
                    print(valueX, valueY, valueZ)
                    print(x,y,z)
                    print(valueX*valueY*valueZ)