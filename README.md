# Dimlitter-zju-dailyhealth-autocheck
利用github action 实现zju自动健康打卡
> 大家有条件的尽量把代码下载到自己仓库运行，最近github action风控较严，觉得有用的话给个star就好啦
## fork自Mrli学长，我只是加了github action 执行功能 还有python写的tg bot推送
Mrli学长原库链接：https://github.com/Freedomisgood/When_Coding_in_ZJU/tree/main/Health_Checkin
<br>交流群组：https://t.me/zjuers </br>
 # 【socks5代理问题暂时无法解决，需要添加socks5代理，实现国内ip访问的请换dev分支】
 ## 需要的secrets(必填)
 > <br>account:浙江大学通行证账号</br>
 > <br>pwd:通行证密码</br>
 > <br>lng:所打卡位置的经度</br>
 > <br>lat:所打卡位置的纬度</br>
 ### 可选 tg bot推送
 ><br>TG_TOKEN:tg bot 的token 通过私聊bot father获得</br>
 ><br>CHAT_ID：你账号的ID</br>

## 更新日志 
### 2021.10.28 pysocks问题无法解决，创建dev分支
### 2021.10.27 添加socks5代理功能，使用国内ip，增加打卡隐蔽性
#### 感谢LittleYe233的大力支持
### 2021.10.24 tg推送模块分离 妄图增加钉钉推送 正在淦 
#### 感谢 zxc2012 增加的平台登录检查功能
### 2021.10.23 添加secrets检查提醒 增加tg bot推送判断 
### 2021.10.20 可用 将持续跟进

## TO DO
### 增加socks5代理功能，以解决github action服务器访问国内网站不稳定的问题（已实现，查看dev分支）
### 实现多样化推送渠道
