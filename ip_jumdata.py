import requests

host = "https://ipaddquery.market.alicloudapi.com/ip/address-query"
appcode = 'ec47729bfe2e4d0f9e4447f73f454f1d'

# 这里采用简单认证；AppCode放到header里就可以了；
def ip(ip):
    headers = {'Authorization':'APPCODE ' + appcode, 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
    response = requests.post(host,data={'ip':ip},headers=headers)
    return response


if __name__ == "__main__":
    ip_adv = "14.123.236.68"
    print(ip(ip_adv).text)
