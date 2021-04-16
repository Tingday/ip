import requests

host = 'https://api01.aliyun.venuscn.com/ip'
appcode = 'ec47729bfe2e4d0f9e4447f73f454f1d'

# 这里采用简单认证；AppCode放到header里就可以了；
def ip(ip):
    headers = {'Authorization':'APPCODE ' + appcode}
    response = requests.get(host,params={'ip':ip},headers=headers)
    return response


