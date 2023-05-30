from PIL import Image
import numpy as np

res = 4096

img = Image.new('1', (res*3, res))

iter = 320

px = img.load()

def logistic_map(a):
    return [np.unique(((i+res)*(res*a[i]-a[i]**2))//(res**2)) for i in range(res*3)]

def logistic_iter(a, d):
    for i in range(d):
        a = logistic_map(a)
    return a

points = list(np.full((res*3,res//2),np.arange(res//2)+1))

for r,rl in enumerate(logistic_iter(points,iter)):
    for i in rl:
        px[r, res-i-1] = 1

img.save('image_unique.bmp')