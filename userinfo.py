import urllib
import urllib.request
import time
import json
import xlwt

id= '7626850687'
# 设置代理IP
proxy_addr = "122.241.72.191:808"

# 定义页面打开函数
def use_proxy(url, proxy_addr):
    req = urllib.request.Request(url)
    req.add_header("User-Agent",
                   "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Mobile Safari/537.36")
    proxy = urllib.request.ProxyHandler({'http': proxy_addr})
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data = urllib.request.urlopen(req).read().decode('utf-8', 'ignore')
    return data


def get_userInfo(id):
    url = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=' + id
    print(url)
    data = use_proxy(url, proxy_addr)
    content = json.loads(data).get('data') #data内容
    profile_image_url = content.get('userInfo').get('profile_image_url')#头像地址
    description = content.get('userInfo').get('description')#微博简介
    profile_url = content.get('userInfo').get('profile_url')#主页地址
    verified = content.get('userInfo').get('verified')#是否认证
    guanzhu = content.get('userInfo').get('follow_count')#关注人数
    name = content.get('userInfo').get('screen_name')#微博昵称
    fensi = content.get('userInfo').get('followers_count')#粉丝数
    gender = content.get('userInfo').get('gender')#性别
    urank = content.get('userInfo').get('urank')#微博等级

    print("微博昵称：" + name + "\n" + "微博主页地址：" + profile_url + "\n" + "微博头像地址：" + profile_image_url + "\n" + "是否认证：" + str(
        verified) + "\n" + "微博说明：" + description + "\n" + "关注人数：" + str(guanzhu) + "\n" + "粉丝数：" + str(
        fensi) + "\n" + "性别：" + gender + "\n" + "微博等级：" + str(urank) + "\n")
    return name


if __name__ == "__main__":
    name = get_userInfo(id)
