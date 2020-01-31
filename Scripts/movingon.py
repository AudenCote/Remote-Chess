import math

mm_per_step = .2717475
boardWidth = 516.5
boardHeight = 426.5


def distance(point1, point2):
    return math.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)


def plotSteps(startCoords, endCoords, numBreaks):
    stepPlot = []  # Motor, direction
    points = []
    for i in range(numBreaks + 1):
        points.append([startCoords[0]+i*(endCoords[0]-startCoords[0])/numBreaks,
                       startCoords[1]+i*(endCoords[1]-startCoords[1])/numBreaks])
    r1 = distance([0, 0], startCoords)
    r2 = distance([0, boardHeight], startCoords)
    r3 = distance([boardWidth, boardHeight], startCoords)
    r4 = distance([boardWidth, 0], startCoords)

    for i in range(numBreaks):
        temp_steps = []
        dr1 = distance([0, 0], points[i])-r1
        dr2 = distance([0, boardHeight], points[i])-r2
        dr3 = distance([boardWidth, boardHeight], points[i])-r3
        dr4 = distance([boardWidth, 0], points[i])-r4

        steps1 = math.copysign(math.floor(abs(dr1/mm_per_step)), dr1)
        steps2 = math.copysign(math.floor(abs(dr2/mm_per_step)), dr2)
        steps3 = math.copysign(math.floor(abs(dr3/mm_per_step)), dr3)
        steps4 = math.copysign(math.floor(abs(dr4/mm_per_step)), dr4)

        steps1 = int(steps1)
        steps2 = int(steps2)
        steps3 = int(steps3)
        steps4 = int(steps4)

        mostSteps = abs(steps1)
        if abs(steps2) > abs(steps1):
            mostSteps = abs(steps2)
        if abs(steps3) > abs(steps2):
            mostSteps = abs(steps3)
        if abs(steps4) > abs(steps3):
            mostSteps = abs(steps4)

        for j in range(mostSteps):
            temp_steps.append(['A0', 0])  # Motor A/B, Direction of step(+/- 1)
            temp_steps.append(['A1', 0])
            temp_steps.append(['B0', 0])
            temp_steps.append(['B1', 0])

        for j in range(abs(steps1)):
            temp_steps[4*round(j*mostSteps/steps1)
                       ][1] = math.copysign(1, steps1)
        for j in range(abs(steps2)):
            temp_steps[1+4*round(j*mostSteps/steps2)
                       ][1] = math.copysign(1, steps2)
        for j in range(abs(steps3)):
            temp_steps[2+4*round(j*mostSteps/steps3)
                       ][1] = math.copysign(1, steps3)
        for j in range(abs(steps4)):
            temp_steps[3+4*round(j*mostSteps/steps4)
                       ][1] = math.copysign(1, steps4)

        for ts in temp_steps:
            stepPlot.append(ts)

        r1 += steps1*mm_per_step
        r2 += steps2*mm_per_step
        r3 += steps3*mm_per_step
        r4 += steps4*mm_per_step

    x = (r3**2-r2**2-boardWidth**2)/(-2*boardWidth)
    y = math.sqrt(r1**2-x**2)
    return [stepPlot, x, y]


steps = plotSteps([10, 10], [90, 90], 80)
