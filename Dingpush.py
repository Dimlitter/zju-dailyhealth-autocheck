import requests
import hmac
import urllib.parse
import time
import json
import hashlib
import base64

"""
钉钉 消息推送类
"""

class dingpush():
    def __init__(self,title,content,reminders,DD_BOT_TOKEN,DD_BOT_SECRET):
        self.DD_BOT_TOKEN = DD_BOT_TOKEN
        self.DD_BOT_SECRET= DD_BOT_SECRET #哈希算法验证(可选)

        self.title = title
        self.content = content
        self.reminders = reminders

    def EncryptionPush(self):
        timestamp = str(round(time.time() * 1000))  # 时间戳
        secret_enc = self.DD_BOT_SECRET.encode('utf-8')
        string_to_sign = '{}\n{}'.format(timestamp, self.DD_BOT_SECRET)
        string_to_sign_enc = string_to_sign.encode('utf-8')
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))  # 签名
        print('开始使用 钉钉机器人 推送消息...')

        url = f'https://oapi.dingtalk.com/robot/send?access_token={self.DD_BOT_TOKEN}&timestamp={timestamp}&sign={sign}'
        headers = {'Content-Type': 'application/json;charset=utf-8'}
        data = {
            'msgtype': 'text',
            'text': {'content': f'{self.title}\n\n{self.content}'}
        }
        try:
            r = requests.post(url=url, data=json.dumps(data), headers=headers, timeout=15).json()
            if not r['errcode']:
                print('INFO: 钉钉推送似乎成功了！')
            else:
                print("INFO: 钉钉推送失败！","错误详情："+ r["errmsg"])
        except Exception as e:
            print(f'ERROR: {e}')
            print(' WARNNING: 你好像没配置DD_BOT_TOKEN或者DD_BOT_SECRET?')  
                
    def NormalPush(self):
        url = f'https://oapi.dingtalk.com/robot/send?access_token={self.DD_BOT_TOKEN}' 
        headers = {'Content-Type': 'application/json;charset=utf-8'}
        data = {
        "msgtype": "text",
        "text": {
            "content": f'{self.title}\n\n{self.content}'
            },
        "at": {
            "atMobiles": [self.reminders],
            "isAtAll": False
            }
    }
        try:
            r = requests.post(url,data=json.dumps(data),headers=headers).json()
            if not r['errcode']:
                print("INFO: 钉钉推送似乎成功了")
                
            else:
                print("INFO: 钉钉推送失败！","错误详情："+ r["errmsg"])
        except Exception as e:
            print("好像发生了什么奇怪的问题",f"ERROR: {e}")

    def SelectAndPush(self):
        if self.DD_BOT_SECRET : 
            self.EncryptionPush()
        else :
            self.NormalPush()


if __name__ == '__main__':
    dingpush = dingpush("测试标题","测试内容","18688888888","","")
    dingpush.SelectAndPush()