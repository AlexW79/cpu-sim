from sim.isa import Instruction, OPCODES, JUMPS

# clean up inputs
def clean(raw):
  return raw.split(';')[0].strip()

def parse_line(text, line_no):
  parts = text.replace(',', ' ').split()
  op = parts[0].upper()
  if op not in OPCODES:
    raise SyntaxError(f"Line {line_no}: unknown instruction '{op}'")
  return Instruction(op, parts[1:], line_no)

def assemble(source):
  labels = {} # position 
  lines = [] # line_no, text for exisiting instructions

  # find labels
  for line_no, raw in enumerate(source.splitlines(), start=1):
    text = clean(raw)
    if not text:
      continue
    if ':' in text:
      label, text = text.split(':', 1)
      labels[label.strip()] = len(lines)#
      text = text.strip()
      if not text:
        continue
    lines.append((line_no, text))

  program = []
  for line_no, text in lines:
    instruction = parse_line(text, line_no)
    if instruction.op in JUMPS:
      name = instruction.args[0]
      if name not in labels:
        raise SyntaxError(f"Line {line_no}: unknown label '{name}'")
      instruction.args = [labels[name]]
    program.append(instruction)
  return program

