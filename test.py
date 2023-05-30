import numpy as np

matrix = np.array([[1,1],[0,1]])

print(np.linalg.eig(matrix)[1][:,0])

print(matrix @ np.linalg.eig(matrix)[1][:,0])