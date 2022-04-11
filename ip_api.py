
#*encoding=utf-8
import requests

simplejs = {
"status": "success",
"country": "中国",
"countryCode": "CN",
"region": "SD",
"regionName": "山东省",
"city": "济南市",
"zip": "",
"lat": 36.6512,
"lon": 117.12,
"timezone": "Asia/Shanghai",
"isp": "China Unicom Shandong Province network",
"org": "NanJing XinFeng Information Technologies, Inc.","as": "AS56046 China Mobile communications corporation",
"query": "114.114.114.114"
}

host = "http://ip-api.com/json/"

def ip(ip):
    headers = {'Content-Type':'application/json; charset=UTF-8'}
    response = requests.get(host+ip,params={'lang':'zh-CN'},headers=headers)
    return response



print(ip("114.114.114.114").text)


