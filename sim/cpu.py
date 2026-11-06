class CPU:
  def __init__(self, program):
    self.program = program # instruction list to run
    self.registers = [0] * 8 # R0 to R7
    self.memory = [0] * 64 # 64 slots of memory
    self.pc = 0 # program counter
    self.zero_flag = False # set by CMP when two values are equal
    self.running = True

  def value(self, operand):
    if operand.startswith('#'):
      return int(operand[1:])
    return self.registers[self.register_number(operand)]

  def register_number(self, operand):
    return int(operand.strip('[]')[1:])
  
  
  def step(self):
    # Fetch
    instruction = self.program[self.pc]
    self.pc += 1

    # Decode
    op = instruction.op
    a = instruction.args

    #Execute
    if op == 'MOV':
      self. registers[self.register_number(a[0])] = self.value(a[1])
    elif op == 'ADD':
      self.registers[self.register_number(a[0])] = self.value(a[1]) + self.value(a[2])
    elif op == 'SUB':
      self.registers[self.register_number(a[0])] = self.value(a[1]) - self.value(a[2])
    elif op == 'MUL':
      self.registers[self.register_number(a[0])] = self.value(a[1]) * self.value(a[2])

    elif op == 'CMP':
      self.zero_flag = self.value(a[0]) == self.value(a[1])
    elif op == 'B': 
      self.pc = a[0]
    elif op == 'BEQ':
      if self.zero_flag:
        self.pc = a[0]
    elif op == 'BNE':
      if not self.zero_flag:
        self.pc = a[0]

    elif op == 'LDR':
      address = self.value(a[1].strip('[]'))
      self.registers[self.register_number(a[0])] = self.memory[address]
    elif op == 'STR':
      address = self.value(a[1].strip('[]'))
      self.memory[address] = self.value(a[0])
    elif op == 'HALT':
      self.running = False

  def run(self, trace=False):
    steps = 0
    while self.running:
      if trace:
        ins = self.program[self.pc]
        print(f"PC={self.pc:2}  {ins.op:4} {str(ins.args):18} "
              f"R0-R3={self.registers[:4]}  Z={int(self.zero_flag)}")
      self.step()
      steps += 1
      if steps > 10_000:
        raise RuntimeError("Too many steps, there may be an infinite loop")
    return steps
    