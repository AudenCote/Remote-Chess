from PEC import MPC
import move

for i in range(0, 3):
	move.off(i)

while True:
	move.manual(int(input("motor?: ")), int(input("steps?: ")))