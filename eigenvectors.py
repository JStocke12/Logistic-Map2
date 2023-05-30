from PIL import Image
import numpy as np

res = 512

img = Image.new('1', (res*3, res))
#img = Image.new('1', (res, res))

px = img.load()

def logistic_matrices(a):
    map = ((np.full((res,res*3),np.arange(res*3)+res).T)*(res*a-a**2))//(res**2)
    return np.array([np.array([np.eye(1,res,j,int)[0] for j in i]) for i in map])

def logistic_vects(a):
    #return np.array([np.linalg.eig(m)[1][0] for m in a])
    return np.array([(lambda x:np.dot(x[0],x[1].T))(np.linalg.eig(m.T)) for m in a])

points = np.full((res*3,res),np.arange(res))

#values = np.linalg.eig(logistic_matrices(points)[2])[1]

#print(np.linalg.eig(logistic_matrices(points)[3].T)[0])

#print(np.linalg.eig(logistic_matrices(points)[3].T)[1].T[2])

"""for i in np.linalg.eig(logistic_matrices(points)[2])[1].T:
    print(i)

matr = np.linalg.matrix_power(logistic_matrices(points)[2],10)#[int(res*2.3)],10)

for r in range(res):
    for i in range(res):
        if abs(matr[r][i])>0.01:
            px[r, res-i-1] = 1"""

vects = np.absolute(logistic_vects(logistic_matrices(points)))

for r in range(res*3):
    for i in range(res):
        if abs(vects[r][i])>0.01:
            px[r, res-i-1] = 1

img.save('image_eig.bmp')
#img.save('image_eig1.bmp')