import sys
import time
import requests
import bs4
from bs4 import BeautifulSoup
import json
import xlrd

def getXLS(xls, start, end):

    xlsData = xlrd.open_workbook(xls)
    tables = xlsData.sheets()
    sheetData = tables[0]
    names = sheetData.col_values(start)
    for name in names:
        if names.count(name) > 1:
            names.remove(name)
    otherNames = sheetData.col_values(end)
    for otherName in otherNames:
        if otherNames.count(otherName) > 1:
            otherNames.remove(otherName)
    repeat = [i for i in names if i in otherNames]
    print(repeat)




    
    #if data.count(child) > 1:
    #    data.remove(child)

start = 3
end = 7
xls = 'byrbt.xls'
getXLS(xls, start, end)

    
