import move
from PEC import MCP

for i in range(0, 4):
	move.off(i)

mcp = MCP()

while True:
	inputtext = input("motor: ")
	inputsteps = input("steps: ")
	if inputtext == "":
		break
	else:
		move.manual(inputtext, inputsteps)