import requests
import re
import threading
import time

class ProxyIP:
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    }
    url = 'https://www.xicidaili.com/nn/'
    checkIPurl = 'http://www.baidu.com'
    index = 1
    ProxiesData = []
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
                t = threading.Thread(target=self.checkIP,args=(self,PreData))
                t.start()
            t.join()
        except:
            print('Get proxy IP failed!')
    def checkIP(self,IP):
        try:
            response = requests.get(url=self.checkIPurl, headers=self.headers,proxies = IP)
            response.raise_for_status()
            self.ProxiesData.append(IP)
            # print(response.status_code,IP,'可用')
        except:
            # print(IP,'不可用')
            pass
    def getProxyIPs(self,num=1):
        while len(self.ProxiesData)<num:
            url = self.url+str(self.index)
            self.getPageProxyIP(self,url=url)
            self.index+=1
        return self.ProxiesData

    def getAProxyIP(self):
        self.getProxyIPs(self)
        return self.ProxiesData[0]

