# Dimlitter-zju-dailyhealth-autocheck
<div style="text-align: center">

 ![AUR](https://img.shields.io/badge/license-MIT%20License%202.0-green.svg)
![GitHub stars](https://img.shields.io/github/stars/Dimlitter/zju-dailyhealth-autocheck.svg?style=social&label=Stars)
![GitHub forks](https://img.shields.io/github/forks/Dimlitter/zju-dailyhealth-autocheck.svg?style=social&label=Fork)

</div>

利用github action 实现自动健康打卡

> 大家有条件的尽量把代码下载到自己仓库运行，最近github action风控较严，觉得有用的话给个star就好啦

## fork自Mrli学长，我只是加了github action 执行功能 还有python写的推送
Mrli学长原库链接：https://github.com/Freedomisgood/When_Coding_in_ZJU/tree/main/Health_Checkin
<br>交流群组：https://t.me/zjuers </br>
## 声明

本项目为Python学习交流的开源非营利项目，仅作为程序员之间相互学习交流之用。

使用者请遵从相关政策。对一切非法使用所产生的后果，我们概不负责。

本项目对您如有困扰请联系我们删除。

## 【socks5代理问题暂时无法解决，需要添加socks5代理，实现国内ip访问的请换dev分支】

## 需要的secrets(必填)
 
 > account:通行证账号
 > 
 > pwd:通行证密码
 > 
 > lng:所打卡位置的经度
 > 
 > lat:所打卡位置的纬度

### 可选 tg bot推送
 
 >TG_TOKEN:tg bot 的token 通过私聊bot father获得
 >
 >CHAT_ID：你账号的ID

## 更新日志 
### 2021.12.05 更新打卡参数
### 2021.11.27 打卡界面发生变化 无需更新仍可使用
### 2021.10.28 pysocks问题无法解决，创建dev分支
### 2021.10.27 添加socks5代理功能，使用国内ip，增加打卡隐蔽性
#### 感谢LittleYe233的大力支持
### 2021.10.24 tg推送模块分离 
#### 感谢 zxc2012 增加的平台登录检查功能
### 2021.10.23 添加secrets检查提醒 增加tg bot推送判断 

## TO DO
 - [x] 增加socks5代理功能，以解决github action服务器访问国内网站不稳定的问题（已实现，查看dev分支）
 - [ ] 实现多样化推送渠道
 - [ ] 模拟真实打卡UA/随机UA
