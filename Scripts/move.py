import time
import math

mm_per_step = 0.5
boardHeight = 100  # mm, distance i-hook to i-hook
boardWidth = 100  # mm, distance i-hook to i-hook

def distance(point1, point2):
	return math.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)

def plotSteps(startCoords, endCoords):

    # [0] = motor id
    # [1] = mm to travel
    # [2] = direction of travel
    # [3] = steps traveled

    print('start:  ', startCoords, 'end:  ', endCoords)

    motor1_info = [1, distance([0, 0], endCoords)-distance([0, 0], startCoords), 0, 0]
    motor2_info = [2, distance([0, boardHeight], endCoords)-distance([0, boardHeight], startCoords), 0, 0]
    motor3_info = [3, distance([boardWidth, boardHeight], endCoords)-distance([boardWidth, boardHeight], startCoords), 0, 0]
    motor4_info = [4, distance([boardWidth, 0], endCoords)-distance([boardWidth, 0], startCoords), 0, 0]

    motor1_info[2] = abs(motor1_info[1])/motor1_info[1]
    motor2_info[2] = abs(motor2_info[1])/motor2_info[1]
    motor3_info[2] = abs(motor3_info[1])/motor3_info[1]
    motor4_info[2] = abs(motor4_info[1])/motor4_info[1]

    motor1_info[3] = math.floor(motor1_info[1]/mm_per_step)
    motor2_info[3] = math.floor(motor2_info[1]/mm_per_step)
    motor3_info[3] = math.floor(motor3_info[1]/mm_per_step)
    motor4_info[3] = math.floor(motor4_info[1]/mm_per_step)

    print(motor1_info, motor3_info)

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
        if i % 4 == 0:
            steps.append(['A1', 0])
        if i % 4 == 1:
            steps.append(['A2', 0])
        if i % 4 == 2:
            steps.append(['B1', 0])
        if i % 4 == 3:
            steps.append(['B2', 0])

    for i in range(motor1_info[3]):
        steps[4*round(i*mostSteps[3]/motor1_info[3])][1] = motor1_info[2]
    for i in range(motor2_info[3]):
        steps[1+4*round(i*mostSteps[3]/motor2_info[3])][1] = motor2_info[2]
    for i in range(motor3_info[3]):
        steps[2+4*round(i*mostSteps[3]/motor3_info[3])][1] = motor3_info[2]
    for i in range(motor4_info[3]):
        steps[3+4*round(i*mostSteps[3]/motor4_info[3])][1] = motor4_info[2]

    return [steps, motor1_info, motor2_info, motor3_info, motor4_info]


def fullPlot(startCoords, endCoords, numBreaks):
    subPoints = []
    x_dist = endCoords[0]-startCoords[0]
    y_dist = endCoords[1]-startCoords[1]
    steps_plot = []

    for i in range(numBreaks+1):
        subPoints.append([i*x_dist/numBreaks + startCoords[0],
                          i*y_dist/numBreaks + startCoords[1]])
        
    next_start_x = startCoords[0]
    next_start_y = startCoords[1]

    steps_traveled1 = 0
    steps_traveled2 = 0
    steps_traveled3 = 0
    steps_traveled4 = 0

    r1 = distance([0, 0], startCoords)
    r2 = distance([0, boardHeight], startCoords)
    r3 = distance([boardWidth, boardHeight], startCoords)

    for p in range(numBreaks):
        plot = plotSteps([next_start_x, next_start_y], subPoints[p+1])

        steps_traveled1 += plot[1][3]
        steps_traveled2 += plot[2][3]
        steps_traveled3 += plot[3][3]

        for s in plot[0]:
            steps_plot.append(s)

        r1 += steps_traveled1*mm_per_step
        r2 += steps_traveled2*mm_per_step
        r3 += steps_traveled3*mm_per_step

        # print('steps by motors: ', steps_traveled1, steps_traveled2, steps_traveled3, steps_traveled4)
        # print('r1, r2, r3: ', r1, r2, r3)

        # got these numbers by solving the equations of circle 1, 2, and 3
        next_start_x = (r3**2-r2**2-boardWidth**2)/(-2*boardWidth) # where is it actually, not rounded?
        next_start_y = math.sqrt(r1**2-next_start_x**2)
        # print(next_start_x, next_start_y)

    return steps_plot

steps = fullPlot([45, 45], [55, 55], 10)
# for s in range(len(steps)):
#    print(steps[s], end='')
#    if s%4 == 3:
#        print('')

   #subtracting platform/2 messes signs


       # motor1_info = [1, distance([0, 0], [endCoords[0]-platformWidth/2, endCoords[1]-platformHeight/2]) -
    #                distance([0, 0], [startCoords[0]-platformWidth/2, startCoords[1]-platformHeight/2]), 0, 0]
    # motor2_info = [2, distance([0, boardHeight], [endCoords[0]-platformWidth/2, endCoords[1]+platformHeight/2]) -
    #                distance([0, boardHeight], [startCoords[0]-platformWidth/2, startCoords[1]+platformHeight/2]), 0, 0]
    # motor3_info = [3, distance([boardWidth, boardHeight], [endCoords[0]+platformWidth/2, endCoords[1]+platformHeight/2]) -
    #                distance([boardWidth, boardHeight], [startCoords[0]+platformWidth/2, startCoords[1]+platformHeight/2]), 0, 0]
    # motor4_info = [4, distance([boardWidth, 0], [endCoords[0]+platformWidth/2, endCoords[1]-platformHeight/2]) -
    #                distance([boardWidth, 0], [startCoords[0]+platformWidth/2, startCoords[1]-platformHeight/2]), 0, 0]
