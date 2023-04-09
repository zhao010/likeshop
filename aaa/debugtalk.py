
import time
import os
import requests


def ENV(keyname):
    values = os.environ.get(keyname,"")
    return values

def sleep(n_secs):
    time.sleep(n_secs)

def login():
    url = "http://sc.xinchengchuansheng.com/api/account/login"
    headers = {"Content-Type":"application/json; charset=utf-8"}
    json = {
	"account": "17600570788",
	"password": "3edc$RFV",
	"client": 6
}
    res = requests.post(url=url,headers=headers,json=json)
    #{"code":1,"msg":"登录成功","data":{"id":2,"nickname":"用户75512691","avatar":"http:\/\/sc.xinchengchuansheng.com\/static\/common\/image\/default\/user.png","level":0,"disable":0,"distribution_code":"6EQ5FU","token":"60bfc94dcaec11e51abb410164e2a5ee"},"show":0,"time":"0.038182"}

    a = res.json()["data"]["token"]
    print(a)
    return a


if __name__ == '__main__':
    login()
