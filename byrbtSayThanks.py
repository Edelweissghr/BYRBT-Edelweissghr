import requests

def sayThanks(URL, start, end):
    url = URL + '/thanks.php'
    myCookies = {'_ga': 'GA1.2.1744326621.1557064441',
               '_gid': 'GA1.2.860613550.1557064441',
               'byrbta': '0',
               'c_secure_login': 'bm9wZQ%3D%3D',
               'c_secure_pass': '74c382f7d11a80eb7223a13bf0a2520b',
               'c_secure_ssl': 'eWVhaA%3D%3D',
               'c_secure_tracker_ssl': 'bm9wZQ%3D%3D',
               'c_secure_uid': 'MjUxMjQ4'
               }
    myHeaders = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36 ",
                 "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8"}

    for n in range(start, end):
        r = requests.post(url, data={'id': str(n)}, cookies = myCookies, headers = myHeaders)
        print(str(n) + '\n')
    
    

URL = 'https://bt.byr.cn'
sayThanks(URL, 261173, 300000)
#284730

    
