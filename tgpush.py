import requests
 
"""
TG 消息推送模块
"""

def post_tg(message, CHAT_ID, TG_TOKEN):
    telegram_message = f"{message}" # 消息内容
               
    params = (
        ('chat_id', CHAT_ID),
        ('text', telegram_message),
        ('parse_mode', "Markdown"), #可选Html或Markdown
        ('disable_web_page_preview', "no")
    )    
    telegram_url = "https://api.telegram.org/bot" + TG_TOKEN + "/sendMessage"
    try:
        telegram_req = requests.post(telegram_url, params=params)
        telegram_status = telegram_req.status_code
        if telegram_status == 200:
            print("INFO: Telegram 消息发送成功！")
        else:
            print("INFO: Telegram 消息发送失败")
    except Exception as e:
        print(f"ERROR: {e}")
        print(" WARNNING: 你好像没配置TG_TOKEN或者CHAT_ID?")
        
if __name__ == "__main__":
    post_tg('浙江大学每日健康打卡 V2.0 '+ " \n\n 签到结果")    
 
