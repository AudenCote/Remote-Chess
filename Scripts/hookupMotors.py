import move
from PEC import MCP

for i in range(0, 4):
	move.off(i)

mcp = MCP()

while True:
	inputtext = input("Custom output (enter to break): ")
	if inputtext == "":
		break
	else:
		mcp.out(inputtext)