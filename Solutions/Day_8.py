import operator
ops = { "+": operator.add, "-": operator.sub }

def ReadInput():
    with open('./InputData/Day_8.txt') as reader:
        return reader.read().replace(' ', '').splitlines()

def ExecuteInstruction(instruction, inputValue):
  global step
  global accumulator
  methods = {
    "acc": lambda x: ops[x[:1]](accumulator, int(x[1:])),
    "jmp": lambda x: ops[x[:1]](step, int(x[1:])),
    "nop": lambda x: step + 1
  }
  if instruction == "acc":
    accumulator = methods[instruction](inputValue)
    step += 1
            
  if instruction == "jmp": 
    step = methods[instruction](inputValue)
                
  if instruction == "nop":
    step = methods[instruction](inputValue)
              
steps = []
step = 0
accumulator = 0
instructions = ReadInput()
while step not in steps:
  steps.append(step)
  instruction = instructions[step]
  ExecuteInstruction(instruction[:3], instruction[3:])
print(accumulator, steps)

