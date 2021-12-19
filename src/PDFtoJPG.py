"""pdf轉jpg"""
from pdf2image import convert_from_path
import os
def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
        # print('-----建立成功-----')

def convert(pdf_dir, img_dir):
    poppler_path = r'.\\Poppler\\poppler-0.68.0_x86\\poppler-0.68.0\\bin'
    try:
        pages = convert_from_path(pdf_dir, 200, poppler_path)
    except:
        print('----pdf is not exist----')
        return
    mkdir(img_dir)
    i = 0
    for page in pages:
        mkdir(img_dir + "\\pdf\\")
        page.save(img_dir + "\\pdf\\" + str(i) + ".jpg", 'JPEG')
        i += 1


