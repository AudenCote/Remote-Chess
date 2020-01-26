import time, math

mm_per_step = 0.543495
boardHeight = 3	#mm, distance i-hook to i-hook
boardWidth = 4	#mm, distance i-hook to i-hook
platformWidth = 45
platformHeight = 45

def distance(coords_1, coords_2):
	return math.sqrt((coords_1[0]-coords_2[0])**2+(coords_1[1]-coords_2[1])**2)

def plotSteps(startCoords, endCoords):

	#[0] = motor id
	#[1] = mm traveled
	#[2] = direction of travel
	#[3] = steps traveled
	motor1_info = [1, distance([0, 0], [endCoords[0]-platformWidth/2, endCoord[1]-platformHeight/2]) - distance([0, 0], [startCoords[0]-platformWidth/2, startCoords[1]-platformHeight/2]), 0, 0]
	motor2_info = [2, distance([0, boardHeight], [endCoords[0]-platformWidth/2, endCoord[1]+platformHeight/2]) - distance([0, boardHeight], [startCoords[0]-platformWidth/2, startCoords[1]+platformHeight/2]), 0, 0]
	motor3_info = [3, distance([boardWidth, boardHeight], [endCoords[0]+platformWidth/2, endCoord[1]+platformHeight/2]) - distance([boardWidth, boardHeight], [startCoords[0]+platformWidth/2, startCoords[1]+platformHeight/2]), 0, 0]
	motor4_info = [4, distance([boardWidth, 0], [endCoords[0]+platformWidth/2, endCoord[1]-platformHeight/2]) - distance([boardWidth, 0], [startCoords[0]+platformWidth/2, startCoords[1]-platformHeight/2]), 0, 0]

	motor1_info[2] = abs(motor1_info[1])/motor1_info[1]
	motor2_info[2] = abs(motor2_info[1])/motor2_info[1]
	motor3_info[2] = abs(motor3_info[1])/motor3_info[1]
	motor4_info[2] = abs(motor4_info[1])/motor4_info[1]

	motor1_info[3] = abs(round(motor1_info[1]/mm_per_step))
	motor2_info[3] = abs(round(motor2_info[1]/mm_per_step))
	motor3_info[3] = abs(round(motor3_info[1]/mm_per_step))
	motor4_info[3] = abs(round(motor4_info[1]/mm_per_step))

	totalSteps = motor1_info[3]+motor2_info[3]+motor3_info[3]+motor4_info[3]
	steps = []

	mostSteps = motor1_info
	if motor2_info[3] > mostSteps[3]:
		mostSteps = motor2_info
	if motor3_info[3] > mostSteps[3]:
		mostSteps = motor3_info
	if motor4_info[3] > mostSteps[3]:
		mostSteps = motor4_info

	for i in range(mostSteps[3]*4):
		if i%4 == 0:
			steps.append(['A1', 0])
		if i%4 == 1:
			steps.append(['A2', 0])
		if i%4 == 2:
			steps.append(['B1', 0])
		if i%4 == 3:
			steps.append(['B2', 0])

	for i in range(motor1_info[3]):
		steps[4*round(i*mostSteps[3]/motor1_info[3])][1] = motor1_info[2]
	for i in range(motor2_info[3]):
		steps[1+4*round(i*mostSteps[3]/motor2_info[3])][1] = motor2_info[2]
	for i in range(motor3_info[3]):
		steps[2+4*round(i*mostSteps[3]/motor3_info[3])][1] = motor3_info[2]
	for i in range(motor4_info[3]):
		steps[3+4*round(i*mostSteps[3]/motor4_info[3])][1] = motor4_info[2]

	return steps