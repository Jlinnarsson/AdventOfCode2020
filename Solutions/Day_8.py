import operator
ops = { "+": operator.add, "-": operator.sub }

def ReadInput():
    with open('./InputData/Day_8.txt') as reader:
        return reader.read().replace(' ', '').splitlines()

def ExecuteInstructions(instructions):
  step = 0
  accumulator = 0
  steps = {}
  while step not in steps.keys() and step < len(instructions):
    instruction = instructions[step]
    steps.update({step: instruction[:3]})
    if instruction[:3] == "acc":
      accumulator = ops[instruction[3:][:1]](accumulator, int(instruction[3:][1:]))
      step += 1       
    if instruction[:3] == "jmp": 
      step = ops[instruction[3:][:1]](step, int(instruction[3:][1:]))   
    if instruction[:3] == "nop":
      step += 1
  return accumulator, step

instructions = ReadInput()
print('Part 1:', ExecuteInstructions(instructions)[0])

for i, value in enumerate(instructions):
  tempInstructions = []
  tempInstructions.extend(instructions)
  if value[:3] == 'jmp':
    tempInstructions[i] = tempInstructions[i].replace('jmp', 'nop')
  elif value[:3] == 'nop':
    tempInstructions[i] = tempInstructions[i].replace('nop', 'jmp')
  else:
    continue
  data = ExecuteInstructions(tempInstructions)
  if data[1] == len(instructions):
    print('Part 2:', data[0])
    break

  

#Part 1
#print(accumulator)

