import urllib.request
import zipfile
import csv

url='https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/csv/zip'
zipName = 'UbikeSta.zip'
urllib.request.urlretrieve(url, zipName)

zFile = zipfile.ZipFile(zipName)
unzipDir = './'
for fileName in zFile.namelist():
    zFile.extract(fileName, unzipDir)
    print(fileName)
zFile.close()

zFile = open(fileName, 'r', encoding='UTF-8')
plots = csv.reader(zFile, delimiter=',')
for row in plots:
    if row[12] != 'bemp' and int(row[12]) >= 10:
        print('%5s' %row[0], '%15s' %row[1], '%5s' %row[3], '%5s' %row[12])
zFile.close()