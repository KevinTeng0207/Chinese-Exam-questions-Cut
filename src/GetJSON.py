import zipfile
from Config import config

pdfdir, pdfname, problemMax = config()
try:
    with zipfile.ZipFile('AdobePDFservicesSDK/output/' + pdfname + '.zip', 'r') as zip_ref:
        zip_ref.extractall('json/' + pdfname + '/')
except:
    print("----zip is not exist")
