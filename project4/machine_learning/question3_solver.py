import math
class Question3_Solver:
    def __init__(self):
        return;

    # Add your code here.
    # Return the centroids of clusters.
    # You must use [(30, 30), (150, 30), (90, 130)] as initial centroids
    
    #calculate the distance between the centro and every points and get the new centro point
    def getNewCentro(self, centroids, points):
		cluster1 = [[],[],[]]
		for j in range(len(points)):
			p = -1
			mini = 1000000000
			for i in range(len(centroids)):
				temp = (points[j][0]-centroids[i][0])**2 + (points[j][1]-centroids[i][1])**2
				if mini > temp:
					mini = temp
					p = i
			cluster1[p].append(points[j])
		newcentro = [(0,0),(0,0),(0,0)]
		for i in range(len(cluster1)):
			count = [0,0]
			for j in range(2):
				for k in range(len(cluster1[i])):
					count[j] = count[j]+cluster1[i][k][j]
			newcentro[i] = (1.0*count[0]/len(cluster1[i]), 1.0*count[1]/len(cluster1[i]))
		return newcentro;

	#get the final centro point using recursion method
    def subSolve(self, previousCentro, points):
		centroids = previousCentro
		newcentro = self.getNewCentro(centroids, points)
		difference = []
		for i in range(len(newcentro)):
			difference.append(math.sqrt((newcentro[i][0]-centroids[i][0])**2 + (newcentro[i][1]-centroids[i][1])**2))
		if difference[0] == 0.0 and difference[1] == 0.0 and difference[2] == 0.0:
			return newcentro
		else:
			centroids = newcentro
			return self.subSolve(centroids, points)

    def solve(self, points):
		centroids = [(30, 60), (150, 60), (90, 130)];
		newcentro = self.getNewCentro(centroids, points)
		difference = []
		for i in range(len(newcentro)):
			difference.append(math.sqrt((newcentro[i][0]-centroids[i][0])**2 + (newcentro[i][1]-centroids[i][1])**2))
		if difference[0] == 0.0 and difference[1] == 0.0 and difference[2] == 0.0:
			return newcentro
		else:
			centroids = newcentro
			return self.subSolve(centroids, points)
			

