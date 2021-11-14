import requests
import hmac
import urllib.parse
import time
import json
import hashlib
import base64

DD_BOT_TOKEN = os.getenv("DD_BOT_TOKEN")
DD_BOT_SECRET=os.getenv("DD_BOT_SECRET") #哈希算法验证(可选)
  
def dingding_bot(title, content):
    timestamp = str(round(time.time() * 1000))  # 时间戳
    secret_enc = DD_BOT_SECRET.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, DD_BOT_SECRET)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))  # 签名
    print('开始使用 钉钉机器人 推送消息...', end='')
    url = f'https://oapi.dingtalk.com/robot/send?access_token={DD_BOT_TOKEN}&timestamp={timestamp}&sign={sign}'
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data = {
        'msgtype': 'text',
        'text': {'content': f'{title}\n\n{content}'}
    }
    response = requests.post(url=url, data=json.dumps(data), headers=headers, timeout=15).json()
    if not response['errcode']:
        print('推送成功！')
    else:
        print('推送失败！')
         
def post_ding(url,reminders,msg):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data = {
    "msgtype": "text",
    "text": {
        "content": msg
    },
    "at": {
        "atMobiles": [   #此处为需要@什么人
    
        ],
        "isAtAll": False
    }
}
    r = requests.post(url,data=json.dumps(data),headers=headers)
    return r.text

if __name__ == '__main__':
    if DD_BOT_SECRET == "" : 
        msg = "测试内容" 
        reminders = ['']
        url = f'https://oapi.dingtalk.com/robot/send?access_token={DD_BOT_TOKEN}' 
        print(post_ding(url, reminders, msg))
    else :
        title = "浙江大学健康打卡"
        content = "钉钉密钥方式推送"
        dingding_bot(title,content)
