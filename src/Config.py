import json
# config read
def config():
    with open('config/config.json', encoding="utf-8") as jsonfile:
        temp = json.load(jsonfile)
        pdfdir = temp['pdfdir']
        pdfname = temp['pdfname']
        problemMax = temp['problemMAX']
    return pdfdir, pdfname, problemMax