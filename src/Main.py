import json
import os
import re
from PIL import Image

from PDFtoJPG import convert
import shutil

# config read
with open('config.json', encoding="utf-8") as jsonfile:
    temp = json.load(jsonfile)
    pdfdir = temp['pdfdir']
    pdfname = temp['pdfname']
    problemMAX = temp['problemMAX']

with open('resources\\' + pdfname + '.json', encoding="utf-8") as jsonfile:
    data = json.load(jsonfile)
    
# pdf to jpg
convert('resources\\' + pdfdir, "output\\" + pdfname) 

def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
        # print('-----建立成功-----')
    else:
        shutil.rmtree(path)
        os.makedirs(path)

def CUT(page, problem, coopery1, coopery2):
    img = Image.open("output\\" + pdfname + '\\pdf\\' + str(page) + '.jpg')
    # print(img.size)
    d = img.size[1] / 842
    y1 = 842 - coopery1
    y2 = 842 - coopery2
    print(y1, y2) # convert 後的座標(y軸)
    # crop((left, upper, right, lower))
    cropped = img.crop((0, y2 * d, img.size[0], y1 * d)) 
    cutimg = "output\\" + pdfname + '\\cut\\' + str(problem - 1) + '.jpg'
    cropped.save(cutimg)


output = []
y1 = 0
y2 = 0
Problem = 0
mixdata = []
mkdir("output\\" + pdfname + '\\cut')
for d in data['elements']:
    try: 
        if re.match(r"^\d{1,}[.][^0-9]", d['Text'] + "測試") is not None:
            Problem = Problem + 1   
            if Problem > problemMAX:
                break
            y2 = d['Bounds'][3]
            # print(d['Bounds'])
            # print("Page = " +  str(d['Page']))
            # print("Problem Number = " + str(Problem))
            print(d['Text'])
            mixdata.append([d['Page'], Problem, y1, y2])
        sub = d['Path'].split('Table') # Table 內容濾掉 不輸出
        if sub[0] == d['Path']:
            output.append(d['Text'] + '\n')
    except:
        output.append('---Have Figure or Table---\n')
        print('---Have Figure or Table---')
    try:
        if Problem >= 1:
            mixdata[Problem - 1][2] = d['Bounds'][1]
    except:
        output.append('---No coordinate---\n')
        print('---No coordinate---')
        continue
    
# output into txt
f = open("output\\" + pdfname + '\\output.txt', 'w', encoding="utf-8")
f.writelines(output)
f.close()

for page, id, y1, y2 in mixdata:
    print(page, id, y1, y2)
    CUT(page, id, y1, y2)


