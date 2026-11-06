import sys
from sim.assembler import assemble
from sim.cpu import CPU

filename = sys.argv[1]
trace = '--trace' in sys.argv

with open(filename) as f:
  program = assemble(f.read())

cpu = CPU(program)
steps = cpu.run(trace=trace)

print(f"Finished after {steps} instructions")
print("Registers:", cpu.registers)