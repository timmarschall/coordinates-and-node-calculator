import datetime
from operator import itemgetter
print('Enter the total length (or height, it is a square you know):')
# we need to work with two decimals here so that's why we use 100
totalGridLength = int(input()) * 100

print('Enter the amount of squares per row. needs to make sense.')
squaresPerRow = int(input())
distanceBetweenPoints = totalGridLength / squaresPerRow

print('use dumb mode? (by default it does not use dumb mode) (y/n)')
useDumbModeString = raw_input()
dumbMode = False

if 'y' in useDumbModeString or 'yes' in useDumbModeString:
	dumbMode = True
	print('Using dumb mode')
else:
	print('using normal sane mode')

pointNumber = 0

coordinateString = ""

nodeString = ""

coordinateArray = []


def addNodeToString(lowerLeftCorner, lowerRightCorner, upperRightCorner, upperLeftCorner):
	currentNodeString = "{0} {1} {2} {3}\n".format(
		str(lowerLeftCorner[2]),
		str(lowerRightCorner[2]),
		str(upperRightCorner[2]),
		str(upperLeftCorner[2]))
	global nodeString
	nodeString += currentNodeString


def addCoordinateToString(x, y):
	currentCoordinateString = "{0} {1}\n".format(
		str(float(x)/100),
		str(float(y)/100))
	global coordinateString
	coordinateString += currentCoordinateString

	global pointNumber
	pointNumber = pointNumber + 1
	coordinateArray.append([x, y, pointNumber])


if dumbMode:
	# the maximum value of each range needs to be this because we calculate the last column weird
	topOfRange = totalGridLength - distanceBetweenPoints + 1
	# calculate all coordinates except last column and top row for whatever reason
	for y in range(0, topOfRange, distanceBetweenPoints):
		for x in range(0, topOfRange, distanceBetweenPoints):
			addCoordinateToString(x, y)

	# last column except 1,1
	for y in range(0, topOfRange, distanceBetweenPoints):
		addCoordinateToString(totalGridLength, y)

	# then do most of the top row - except the first and last point for whatever goddamn reason
	for x in range(distanceBetweenPoints, 96, distanceBetweenPoints):
		addCoordinateToString(x, totalGridLength)

	# now lets add the last two points
	addCoordinateToString(totalGridLength, totalGridLength)
	addCoordinateToString(0, totalGridLength)
else:
	# calculate all coordinates left to right bottom to top like a normal person
	for y in range(0, totalGridLength + 1, distanceBetweenPoints):
		for x in range(0, totalGridLength + 1, distanceBetweenPoints):
			addCoordinateToString(x, y)

# sort the damn thing by y and then x so we can iterate left to right, bottom to top
sortedCoordinateList = sorted(coordinateArray, key=itemgetter(1, 0))

# none of these -1 values matters, but I needed to initialize them
lowerLeftCornerIdx = -1
lowerRightCornerIdx = -1
upperLeftCornerIdx = -1
upperRightCornerIdx = -1

pointsPerRow = squaresPerRow + 1

for row in range(0, squaresPerRow):
	lowerLeftCornerIdx = row * pointsPerRow
	lowerRightCornerIdx = lowerLeftCornerIdx + 1
	upperLeftCornerIdx = lowerLeftCornerIdx + pointsPerRow
	upperRightCornerIdx = upperLeftCornerIdx + 1
	for column in range(0, squaresPerRow):
		addNodeToString(sortedCoordinateList[lowerLeftCornerIdx], sortedCoordinateList[lowerRightCornerIdx],
		                sortedCoordinateList[upperRightCornerIdx], sortedCoordinateList[upperLeftCornerIdx])
		lowerLeftCornerIdx += 1
		lowerRightCornerIdx += 1
		upperRightCornerIdx += 1
		upperLeftCornerIdx += 1

# write two files - one for coordinates and one for nodes
filenameCoordinates = "py_coordinates_{0}_{1}.dat".format(
	'dumb' if dumbMode else 'normal', # add whether it's been made dumb or smart
	str(datetime.datetime.now().strftime('%Y_%m_%d_%H_%M'))) # add timestamp
filenameNodes = "py_nodes_{0}_{1}.dat".format(
	'dumb' if dumbMode else 'normal', # add whether it's been made dumb or smart
	str(datetime.datetime.now().strftime('%Y_%m_%d_%H_%M'))) # add timestamp

coordinateFile = open(filenameCoordinates, "w")
coordinateFile.write(coordinateString)

nodeFile = open(filenameNodes, "w")
nodeFile.write(nodeString)
print('Finished. Files written as:\n {0} \n {1}'.format(filenameCoordinates, filenameNodes))
