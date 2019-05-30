import requests

def sayThanks(URL, start, end):
    url = URL + '/thanks.php'
    
    #填写自己的cookie信息
    myCookies = {'_ga': '',
               '_gid': '',
               'byrbta': '',
               'c_secure_login': '',
               'c_secure_pass': '',
               'c_secure_ssl': '',
               'c_secure_tracker_ssl': '',
               'c_secure_uid': ''
               }
    
    #设置请求头
    myHeaders = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 ",
                 "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8"}

    #提交post请求
    for n in range(start, end):
        r = requests.post(url, data={'id': str(n)}, cookies = myCookies, headers = myHeaders)
        print(str(n) + '\n')
    
    

URL = 'https://bt.byr.cn'

#id从261173到300000开始执行
sayThanks(URL, 261173, 300000)
#284730
