from PIL import Image
img = Image.open('output\\test2\\pdf\\0.jpg')
print(img.size)
# crop((left, upper, right, lower))
y1 = 438.0254364013672 # 選項的y1
y2 = 500.6990356445312 # 題目頭的y2
y1 = 842 - y1
y2 = 842 - y2
d = img.size[1] / 842
print(y2 * d, y1 * d)
print(d)
cropped = img.crop((0, y2 * d, img.size[0], y1 * d)) 
name = 'output\\test2\\cut\\0111.jpg'
cropped.save(name)