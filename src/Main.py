import json
import os
import re
from PIL import Image
from PDFtoJPG import convert
import shutil
from Config import config
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger

pdfdir, pdfname, problemMax = config()
with open('../json/' + pdfname + '/structuredData.json', encoding="utf-8") as jsonfile:
    data = json.load(jsonfile)
    
# pdf to jpg
convert('../resources/' + pdfdir, "../CutOutput/" + pdfname) 

def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
        # print('-----建立成功-----')
    else:
        shutil.rmtree(path)
        os.makedirs(path)

def CUT(page, problem, coopery1, coopery2):
    pdf_file = PdfFileReader(open("../resources/" + pdfdir,"rb"))
    mypage = pdf_file.getPage(0)
    # print(mypage.cropBox.getUpperRight())
    maxsizeX = int(mypage.cropBox.getUpperRight()[0])
    maxsizeY = int(mypage.cropBox.getUpperRight()[1])
    # print(maxsizeX, maxsizeY)
    img = Image.open("../CutOutput/" + pdfname + '/pdf/' + str(page) + '.jpg')
    # print(img.size)
    d = img.size[1] / maxsizeY
    y1 = maxsizeY - coopery1
    y2 = maxsizeY - coopery2
    # print(y1, y2) # convert 後的座標(y軸)
    cropped = img.crop((0, y2 * d, img.size[0], y1 * d)) # crop((left, upper, right, lower))
    cutimg = "../CutOutput/" + pdfname + '/cut/' + str(problem - 1) + '.jpg'
    cropped.save(cutimg)


output = []
y1 = 0
y2 = 0
Problem = 0
mixdata = []
mkdir("../CutOutput/" + pdfname + '/cut')
for d in data['elements']:
    try:
        # "^[(][ ][)]\d{1,}[.]"
        # "^\d{1,}[.][^0-9]" 
        if re.match(r"^\d{1,}[.][^0-9]", d['Text'] + "測試") is not None:
            Problem = Problem + 1   
            if Problem > problemMax:
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
f = open("../CutOutput/" + pdfname + '/output.txt', 'w', encoding="utf-8")
f.writelines(output)
f.close()

# print(mixdata)
for page, id, y1, y2 in mixdata:
    print('第%s頁 第%s題 y1 = %f y2 = %f' % (page + 1, id, y1, y2))
    CUT(page, id, y1, y2)

