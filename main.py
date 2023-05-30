from PIL import Image
import numpy as np

res = 4069

img = Image.new('1', (res*3, res))

iter = 640

px = img.load()

def logistic_map(a):
    #return ((np.full((res//2,res*3),np.arange(res*3)+res).T)*(res*a-a**2))//(res**2)
    return ((np.arange(res * 3) + res)[:,None] * (res * a - a ** 2)) // (res ** 2)

def logistic_iter(a, d):
    for i in range(d):
        print(i)
        a = np.sort(logistic_map(a))
    return a

points = np.full((res*3,res//2),np.arange(res//2)+1)

for r,rl in enumerate(logistic_iter(points,iter)):
    for i in rl:
        px[r, res-i-1] = 1

img.save('image.bmp')