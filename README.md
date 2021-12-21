# Chinese-Exam-questions-Cut
## Prerequisites
* Node.js : Version 10.13
* Python : > 3.0 

## Installation

Use the npm(Node.js) to install modules

### node_modules Installation

```bash
cd AdobePDFservicesSDK/
npm install
```

### python Installation
```bash
cd ..
cd src/
pip install -r requirements.txt
```
## Config

pdfdir 跟 pdfname 自行設定
pdfname 跟 pdf 檔名一樣
problemMAX 為 需要抓取的考題數量
```json
{
    "pdfdir": "test.pdf",
    "pdfname": "test",
    "problemMAX": 24 
}
```

## SDK Usage
Put your pdf to resources(Home) folder
and then system will copy your PDf to SDK input folder

```bash
cd src/
python.exe Copy.py
```

Run SDK api to get output

```bash
cd AdobePDFservicesSDK/
node ./src/extractpdf/extract-text-info-from-pdf.js
```

Get structuredData.json to extract pdf infomation

```bash
cd src/
python.exe Getjson.py
```
Final to get cut problem in CutOutput/
```bash
python.exe Main.py
```
## Output
輸出位於 Home 目錄的 Cutoutput 
* output.txt (全文)
* 尚未切割的 jpg
* 切割後的 jpg
## Contributing
For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
### Tool from
https://www.adobe.io/apis/documentcloud/dcsdk/pdf-extract.html
https://www.adobe.io/apis/documentcloud/dcsdk/docs.html
