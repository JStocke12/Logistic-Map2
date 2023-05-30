from PIL import Image

res = int(input("Image size and resolution: "))

iter = int(input("Iteration length: "))

img = Image.new('1', (res*3, res))

px = img.load()

def logistic_map(r, l):
    return [r*i*(1-i) for i in l]

def logistic_iter(r, l, d):
    for i in range(d):
        l = logistic_map(r, l)
    return l

for r in [i/res for i in range(res, res*4)]:
    for i in [j//(1/res) for j in logistic_iter(r, [1-(i/iter) for i in range(iter)], 2*iter)]:
        px[r*res-res, res-i-1] = 1

img.save('image_float.bmp')