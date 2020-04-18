# -*- coding: utf-8 -*-

import requests

'''接口测试，直接测试后端服务，只需要模拟下发的请求，将其提交至服务端，接受服务器给出的响应即可'''

requests.get()  # 发送模拟的get请求
requests.post()  # 发送模拟的post请求

###################################
# get方法
params = {
    'loginName': '111111',
    'pwd': '123456'
}
url = 'http://localhost:8080/interface/login'

res = requests.get(url, params)
print(res)       #返回状态码
print(res.text)  #返回响应的实际内容
print(res.status_code)
####################################
#post方法



