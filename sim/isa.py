from dataclasses import dataclass

@dataclass
class Instruction:
  op: str # the operation
  args: list # the operands
  line: int # which line of the source file

# Instruction Set
OPCODES = {'MOV', 'ADD', 'SUB', 'MUL', 'LDR', 'STR', 'CMP', 'B', 'BEQ', 'BNE', 'HALT'}

# The instructions which jump to a label
JUMPS = {'B', 'BEQ', 'BNE'} 
