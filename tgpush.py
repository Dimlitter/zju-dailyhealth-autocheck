from requests import post
import os
 
"""
TG 消息推送模块
"""

TG_TOKEN = os.getenv("TG_TOKEN")	#TG机器人的TOKEN
CHAT_ID = os.getenv("CHAT_ID")	    #推送消息的CHAT_ID



def post_tg(message):
    telegram_message = f"{message}"
               
    params = (
        ('chat_id', CHAT_ID),
        ('text', telegram_message),
        ('parse_mode', "Markdown"), #可选Html或Markdown
        ('disable_web_page_preview', "yes")
    )    
    telegram_url = "https://api.telegram.org/bot" + TG_TOKEN + "/sendMessage"
    telegram_req = post(telegram_url, params=params)
    telegram_status = telegram_req.status_code
    if telegram_status == 200:
        print(f"INFO: Telegram Message sent")
    else:
        print("Telegram Error")
        
if __name__ == "__main__":
    post_tg('浙江大学每日健康打卡 V1.0 '+ " \n\n 签到结果: " + res.get("m"))    
 
