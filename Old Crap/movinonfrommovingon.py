import math

mm_per_step = .2717475
boardWidth = 396
boardHeight = 412

def distance(point1, point2):
	return math.sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)

def plotSteps(startCoords, endCoords, numBreaks):
	plot = []
	targets = []
	for i in range(0, numBreaks):
		targets.append([startCoords[0]+(i+1)*(endCoords[0]-startCoords[0])/numBreaks, startCoords[1]+(i+1)*(endCoords[1]-startCoords[1])/numBreaks])
	x = startCoords[0]
	y = startCoords[1]

	r0 = distance([0, 0], startCoords)
	r1 = distance([0, boardHeight], startCoords)
	r2 = distance([boardWidth, boardHeight], startCoords)
	r3 = distance([boardWidth, 0], startCoords)

	for t in targets:
		dr0 = distance([0, 0], t) - distance([0, 0], [x, y])
		dr1 = distance([0, boardHeight], t) - distance([0, boardHeight], [x, y])
		dr2 = distance([boardWidth, boardHeight], t) - distance([boardWidth, boardHeight], [x, y])
		dr3 = distance([boardWidth, 0], t) - distance([boardWidth, 0], [x, y])

		steps0 = int(dr0/mm_per_step)
		steps1 = int(dr1/mm_per_step)
		steps2 = int(dr2/mm_per_step)
		steps3 = int(dr3/mm_per_step)

		plot.append(['A0', steps0], ['A1', steps1], ['B0', steps2], ['B1', steps3])

		r0 += steps0*mm_per_step
		r1 += steps1*mm_per_step
		r2 += steps2*mm_per_step
		r3 += steps3*mm_per_step

		x = (r2**2-r1**2-boardWidth**2)/(-2*boardWidth)
		y = math.sqrt(r0**2-x**2)
	return plot, x, y