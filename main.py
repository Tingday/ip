# flask测试工程
from flask import Flask,request,render_template
import aliyun


app = Flask(__name__)


@app.route('/')
def ip():
    ip = request.remote_addr
    print("ip",ip)
    res = aliyun.ip(ip).json()
    print(res)
    if res['data']:
        country = res['data']['country'] # 中国
        region = res['data']['region']  # 广东
        city = res['data']['city'] # 深圳
        area = res['data']['area'] # 华南
        isp = res['data']['isp'] # 电信
        ip_text = country + region + city
        ip_isp = area + isp
        print("ip物理地址:", res.data)
    else:
        ip_text=""
        msg = res['msg']
        ip_isp=""
        print("msg", res['msg'])

    return render_template("ip.html",ip_addr=ip,ip_text=ip_text,ip_isp=ip_isp,msg = msg)

if __name__ == "__main__":
    print("ip程序启动")
    app.run
