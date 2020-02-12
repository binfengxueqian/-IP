# 获取西刺代理IP

使用步骤

```python
from getProxies import ProxyIP

# 获取一个代理IP
a = ProxyIP
proxies =  a.getAProxyIP()
print(proxies)
#{'HTTP': '111.79.44.185:9999'}

#获取一些代理IP
a = ProxyIP
proxies =  a.getProxyIPs(num = 100)
print(proxies)
'''
[
{'HTTP': '111.79.44.185:9999'},
……
{'HTTP': '111.79.44.185:9999'},
{'HTTP': '111.79.44.185:9999'},
]
'''

#也可以直接从a.ProxiesData中获取

```

```python
from getProxies import ProxyIP
#新增功能
#指定可用性的检查地址为谷歌或者其他地址
A = ProxyIP(checkurl = 'www.google.com.hk')

```