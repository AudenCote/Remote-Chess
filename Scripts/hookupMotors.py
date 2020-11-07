import move

for i in range(0, 4):
	move.off(i)

while True:
	move.manual(int(input("motor?: ")), int(input("steps?: ")))