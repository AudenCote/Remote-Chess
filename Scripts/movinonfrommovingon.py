import math

mm_per_step = 1
boardWidth = 300
boardHeight = 300

def distance(point1, point2):
	return math.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)

def plotSteps(radii, endCoords, numBreaks):
	plot = []
	targets = []
	for i in range(0, numBreaks):
		targets.append([startCoords[0]+(i+1)*(endCoords[0]-startCoords[0])/numBreaks, startCoords[1]+(i+1)*(endCoords[1]-startCoords[1])/numBreaks])

	r0 = radii[0]
	r1 = radii[1]
	r2 = radii[2]
	r3 = radii[3]

	for t in targets:
		dr0 = distance([0, 0], t) - r0
		dr1 = distance([0, boardHeight], t) - r1
		dr2 = distance([boardWidth, boardHeight], t) - r2
		dr3 = distance([boardWidth, 0], t) - r3

		steps0 = int(dr0/mm_per_step)
		steps1 = int(dr1/mm_per_step)
		steps2 = int(dr2/mm_per_step)
		steps3 = int(dr3/mm_per_step)

		for i in range(steps0):
			plot.append(['A0', math.copysign(1, steps0)])
		for i in range(steps1):
			plot.append(['A1', math.copysign(1, steps1)])
		for i in range(steps2):
			plot.append(['B0', math.copysign(1, steps2)])
		for i in range(steps3):
			plot.append(['B1', math.copysign(1, steps3)])

		r0 += steps0*mm_per_step
		r1 += steps1*mm_per_step
		r2 += steps2*mm_per_step
		r3 += steps3*mm_per_step

	return plot, [r0, r1, r2, r3]