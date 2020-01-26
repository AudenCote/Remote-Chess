import time
import math

mm_per_step = 0.543495
boardHeight = 412  # mm, distance i-hook to i-hook
boardWidth = 396  # mm, distance i-hook to i-hook
platformWidth = 45
platformHeight = 45


def distance(coords_1, coords_2):
    return math.sqrt((coords_1[0]-coords_2[0])**2+(coords_1[1]-coords_2[1])**2)


def plotSteps(startCoords, endCoords):

    # [0] = motor id
    # [1] = mm to travel
    # [2] = direction of travel
    # [3] = steps traveled
    motor1_info = [1, distance([0, 0], [endCoords[0]-platformWidth/2, endCoords[1]-platformHeight/2]) -
                   distance([0, 0], [startCoords[0]-platformWidth/2, startCoords[1]-platformHeight/2]), 0, 0]
    motor2_info = [2, distance([0, boardHeight], [endCoords[0]-platformWidth/2, endCoords[1]+platformHeight/2]) -
                   distance([0, boardHeight], [startCoords[0]-platformWidth/2, startCoords[1]+platformHeight/2]), 0, 0]
    motor3_info = [3, distance([boardWidth, boardHeight], [endCoords[0]+platformWidth/2, endCoords[1]+platformHeight/2]) -
                   distance([boardWidth, boardHeight], [startCoords[0]+platformWidth/2, startCoords[1]+platformHeight/2]), 0, 0]
    motor4_info = [4, distance([boardWidth, 0], [endCoords[0]+platformWidth/2, endCoords[1]-platformHeight/2]) -
                   distance([boardWidth, 0], [startCoords[0]+platformWidth/2, startCoords[1]-platformHeight/2]), 0, 0]

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
    for i in range(numBreaks):
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

    for p in range(numBreaks-1):
        print(next_start_x, next_start_y)
        plot = plotSteps([next_start_x, next_start_y], subPoints[p+1])

        steps_traveled1 += plot[1][3]*plot[1][2]
        steps_traveled2 += plot[2][3]*plot[2][2]
        steps_traveled3 += plot[3][3]*plot[3][2]

        for s in plot[0]:
            steps_plot.append(s)

        r1 += steps_traveled1
        r2 += steps_traveled2
        r3 += steps_traveled3

        # these numbers were gotten by solving the equations of circle 1, 2, and 3
        next_start_x = (r3**2-r2**2-boardWidth**2)/(-2*boardWidth)
        # where is it actually, not rounded?
        next_start_y = math.sqrt(r1**2-next_start_x**2)

    return steps_plot
