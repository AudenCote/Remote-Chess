import time
import math
from port_expander_config import MCP

mcp = MCP()

class Motor:

    def __init__(self, reg):
        self.reg = reg
        self.output = [reg, '0', '0', '0', '0', '0', '0', '0', '0']
            
        self.curr_step = 0

        self.step_seq = [
            '1000',
            '1100',
            '0100',
            '0110',
            '0010',
            '0011',
            '0001',
            '1001'
        ]
        

    def move_step(self, direction, iden):
        self.curr_step += 1*direction
        if self.curr_step > 7:
            self.curr_step = 0
        if self.curr_step < 0:
            self.curr_step = 7

        out = ''
        if iden == 0:
            for i in range(4):
                self.output[i+1] = self.step_seq[self.curr_step][i]
            for i in self.output:
                out = out + i
            mcp.output(out)
        elif iden == 1:
            for i in range(4):
                self.output[i+5] = self.step_seq[self.curr_step][i]
            for i in self.output:
                out = out + i
            mcp.output(out)
  

a_motors = Motor('A')
b_motors = Motor('B')

for i in range(10000000):
    a_motors.move_step(1, 1)
    a_motors.move_step(1, 0)
    
    b_motors.move_step(1, 0)
    b_motors.move_step(1, 1)
    
    time.sleep(.002)










