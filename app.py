# flask测试工程
from flask import Flask, request, render_template
import ip_jumdata

app = Flask(__name__)


@app.route('/')
@app.route('/ip')
def ip():
    ip = request.remote_addr
    ip_res = ip_jumdata.ip(ip)
    if not ip_res:
        return render_template("ip.html", ip_addr="访问错误。", msg="IP地址接口过期，请联系管理员")
    else:
        res = ip_res.json()
        pass
    if res['data']:
        country = res['data']['country']  # 中国
        region = res['data']['region']  # 广东
        city = res['data']['city']  # 深圳
        area = res['data']['area']  # 华南
        isp = res['data']['isp']  # 电信
        ip_text = country + region + city
        ip_isp = area + isp
        msg = ""
        # print("ip物理地址:", res['data'])
    else:
        ip_text = ""
        msg = res['msg']
        ip_isp = ""
        # print("msg", res['msg'])

    return render_template("ip.html", ip_addr=ip, ip_text=ip_text, ip_isp=ip_isp, msg=msg)


if __name__ == "__main__":
    print("ip程序启动")
    app.run
