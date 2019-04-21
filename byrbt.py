import sys
import time
import requests
import bs4
from bs4 import BeautifulSoup
import json

# 定义延迟函数
def sleeptime(min, sec = 0):
    return min*60 + sec

# 每次访问时得到页面内免费种ID列表
def getTorrentList(url):
    
	# Chrome可利用"EditThisCookie"插件，得到网站cookie，填入自己的cookie
	cookies = {'_ga': '',
               '_gid': '',
               'byrbta': '',
               'byrbta1': '',
               'byrbta2': '',
               'byrbta3': '',
               'byrbta4': '',
               'c_secure_login': '',
               'c_secure_pass': '',
               'c_secure_ssl': '',
               'c_secure_tracker_ssl': '',
               'c_secure_uid': ''
               }
    
	result = {}
    res = requests.get(url, cookies = cookies)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    # print(soup)
    torrentsList = []
    download = []
    
	# 免费种子的class是'free_bg'，标签为tr
	trs = soup.find_all(class_ = 'free_bg')
    for tr in trs:
        for link in tr.find_all('a'):
            if 'download' in link.get('href'):
                torrentsList.append(link.get('href')[16:])
    
	# 因数组中每个种子id会获得两遍，故去重
	for torrent in torrentsList:
        while torrentsList.count(torrent) > 1:
            torrentsList.remove(torrent)
    # print(torrentsList)
    return torrentsList

# 新数组与旧数组作比较，得到将要下载的种子列表    
def getDownloadList(listOld, listNew):
    for torrent in listNew:
        if torrent not in listOld:
            download.append(torrent)
    return download

# ServerChan (https://sc.ftqq.com/3.version) 向目的网址提交请求	
def send(download):
    
	# 填入自己的SCKEY
	SCKEY = ''
    serverURL = 'http://sc.ftqq.com/' + SCKEY + '.send'
    desp = ''
    
	# 更新免费种子时，则微信推送告知我
	if len(download) != 0:
        for a in download:
            desp += str(a)
            desp += '_'
        # print(desp)
        r = requests.post(url = serverURL, data = {'text': 'byrbt更新免费种啦！', 'desp': desp[:-1]})
    

url = 'https://bt.byr.cn/torrents.php'
listNew = []
second = sleeptime(3) # 延时3分钟
while 1==1:

    # print('time: ', time.asctime(time.localtime(time.time())))
    listOld = listNew
    # print('listOld: ', listOld)
    listNew = getTorrentList(url)
    # print('listNew: ', listNew)
    download = []
    download = getDownloadList(listOld, listNew)
    # print('download: ', download, '\n')
    send(download)
    time.sleep(second)
    
