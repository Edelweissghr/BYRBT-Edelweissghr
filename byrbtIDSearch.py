import sys
import time
import requests
import bs4
from bs4 import BeautifulSoup
import json
import xlwt
import xlrd
#workbook = xlrd.open_workbook('byrbt.xls')
workbook = xlwt.Workbook('byrbt.xls')
table = workbook.add_sheet('2')
table.write(0,0,'username')
table.write(0,1,'invite')
table.write(0,2,'level')
table.write(0,3,'joinDate')
table.write(0,4,'latestDate')
table.write(0,5,'upload')
table.write(0,6,'download')
table.write(0,7,'school')
table.write(0,8,'magic')
table.write(0,9,'sex')
table.write(0,10,'invitePerson')
table.write(0,11,'id')
global row
row = 1
def getURL(firstURL,start,end):
    for n in range(int(start),int(end)):
        url = firstURL + str(n)
        global row
        getUserInfo(url)
    

def getUserInfo(url):
    global row
    cookies = {'_ga': 'GA1.2.1932543224.1540114520',
               '_gid': 'GA1.2.105455741.1552647897',
               'byrbta': '0',
               'byrbta1': '0',
               'byrbta2': '0',
               'byrbta3': '0',
               'byrbta4': '0',
               'c_secure_login': 'bm9wZQ%3D%3D',
               'c_secure_pass': '74c382f7d11a80eb7223a13bf0a2520b',
               'c_secure_ssl': 'eWVhaA%3D%3D',
               'c_secure_tracker_ssl': 'bm9wZQ%3D%3D',
               'c_secure_uid': 'MjUxMjQ4'
               }
    result = {}
    print(url)
    res = requests.get(url, cookies = cookies)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
        
    title = soup.find_all('title')
    username = str(title[0])[23:-30]
    #list = soup.find_all(class_ = 'rowfollow')
    #invite = list[0]
    #invitePerson = list[1].find('a')['class'][0]
    list_ = soup.find_all(class_ = 'outer')[0].find_all('tr')[0]
    
    data = []
    if list_.find_all('h2'):
        pass
    #joinDate = list[1]
    #latestDate = list[2]
    #flow = list[3].find_all('tr')[1]
    #upload = flow.find_all('td')[0]
    #download = flow.find_all('td')[1]
    #sex = list[5].find_all('img')[0]['class'][0]
    #level = list[6].find_all('img')[0]['title']
    # school = list[8]
    if str(username) != '':
        for child in list_.descendants:
            child = str(child.string)
            data.append(child)
            if data.count(child) > 1:
                data.remove(child)
        #if soup.find_all('不存在该ID的用户！'):
        #    pass
        reject = '对不起，访问被用户' + username + '拒绝。用户想要保护其隐私。'
        if reject in data:
            pass
        else:
            invite = 0
            if '邀请' in data:
                invite = data[data.index('邀请')+1]
            invitePerson = None
            if '邀请人' in data:
                invitePerson = data[data.index('邀请人')+1]
            if '加入日期' in data:
                joinDate = data[data.index('加入日期')+1][:-2]
            if '最近动向' in data:
                latestDate = data[data.index('最近动向')+1][:-2]
            upload = data[data.index('上传量')+1][3:]
            download = data[data.index('下载量')+1][3:]
            school = data[data.index('学校')+1]
            magic = data[data.index('魔力值')+1]
            if list_.find_all(class_ = 'male'):
                sex = 'male'
            else:
                sex = 'female'
            if list_.find_all(alt = 'Power User'):
                level = 'Power User'
            elif list_.find_all(alt = 'User'):
                level = 'User'
            elif list_.find_all(alt = 'Peasant'):
                level = 'Peasant'
            elif list_.find_all(alt = 'Elite User'):
                level = 'Elite User'
            elif list_.find_all(alt = 'Crazy User'):
                level = 'Crazy User'
            elif list_.find_all(alt = 'Insane User'):
                level = 'Insane User'
            elif list_.find_all(alt = 'Veteran User'):
                level = 'Veteran User'
            elif list_.find_all(alt = 'Extreme User'):
                level = 'Extreme User'
            elif list_.find_all(alt = 'Ultimate User'):
                level = 'Ultimate User'
            elif list_.find_all(alt = 'Nexus User'):
                level = 'Nexus User'
            else:
                level = 'other'

            table.write(row, 0, username)
            table.write(row, 1, invite)
            table.write(row, 2, level)
            table.write(row, 3, joinDate)
            table.write(row, 4, latestDate)
            table.write(row, 5, upload)
            table.write(row, 6, download)
            table.write(row, 7, school)
            table.write(row, 8, magic)
            table.write(row, 9, sex)
            table.write(row, 10, invitePerson)
            row = row + 1


        #print(str(username)[23:-30])
        #print(str(invite)[48:-5])
            
        # print(str(joinDate)[60:][:19])
        # print(str(latestDate)[60:][:19])
        # print(str(upload)[44:-5])
        # print(str(download)[46:-5])
        # print(str(sex))
        # print(str(level))
        # print(list[8])
        # print(str(school)) # [60:-5]
        # print(magic)
        workbook.save('byrbt.xls')
        print('\n')
    
    # trs = soup.find_all(class_ = 'free_bg')
    # for tr in trs:
    #     for link in tr.find_all('a'):
    #         if 'download' in link.get('href'):
    #             torrentsList.append(link.get('href')[16:])
    # for torrent in torrentsList:
    #     while torrentsList.count(torrent) > 1:
    #         torrentsList.remove(torrent)
    # return torrentsList
    
    

firstURL = 'https://bt.byr.cn/userdetails.php?id='
getURL(firstURL, 291300, 293150)

    
