import requests
import re
import threading
import time
class ProxyIP():
    def __init__(self,checkurl = 'http://www.baidu.com'):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        }
        self.url = 'https://www.xicidaili.com/nn/'
        self.checkIPurl = checkurl
        self.index = 1
        self.ProxiesData = []
    def getPageProxyIP(self,url):
        try:
            response = requests.get(url=url, headers=self.headers)
            response.raise_for_status()
            response.encoding = response.apparent_encoding
            responseTxt = response.text.replace('\n', '')
            TempData = re.findall(
                '  <tr class=.*?<td>(\d+\.\d+\.\d+\.\d+)</td>.*?<td>(\d+)</td>.*?<td>([A-Z]{4,5})</td>.*?</tr>',
                responseTxt)
            PreDatas = []
            for item in TempData:
                PreData = {}
                PreData[item[2]] = item[0] + ':' + item[1]
                PreDatas.append(PreData)
                t = threading.Thread(target=self.checkIP,args=(item[2],item[0] + ':' + item[1]))
                t.start()
            t.join()
        except:
            print('Get proxy IP failed!')
    def checkIP(self,http,ip):
        proxy = {}
        proxy[http] = ip
        IP = proxy.copy()
        try:
            response = requests.get(url=self.checkIPurl, headers=self.headers,proxies = proxy)
            response.raise_for_status()
            self.ProxiesData.append(IP)
            # print(IP,'可用')
        except:
            # print(IP,'不可用')
            pass
    def getProxyIPs(self,num=1):
        while len(self.ProxiesData)<num:
            url = self.url+str(self.index)
            self.getPageProxyIP(url=url)
            self.index+=1
            time.sleep(3)
        return self.ProxiesData

    def getAProxyIP(self):
        self.getProxyIPs()
        return self.ProxiesData[0]

# if __name__ == '__main__':
#     A = ProxyIP()
#     A.getAProxyIP()
#     with open('2.12.json','w',encoding='utf-8')as f:
