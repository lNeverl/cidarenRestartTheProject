import requests#导入request模块
import json
import os
import time
import pyperclip#调用pyperclip模块


ans31mod=['null','null','null','null','null','null','null','null','null','null']
delay=0#定义两个全局变量 后边有用
lastans=0
def readJsonfile():
    a = json.load(open('c:\\cdr\\responseBody.txt', 'r', encoding='UTF-8'))  
    return a

while True:

    a=readJsonfile()
    if "topic_mode" in (a['data']) :
        topic_mode = (a['data']['topic_mode'])
    if "stem" in (a['data']) :
        content = (a['data']['stem']['content'])
        remark = (a['data']['stem']['remark'])
    token = 'a9a37f2b6444902fbc469491c17fc260'
    if "topic_mode" in (a['data']) :
        if topic_mode == 31 :
            lenth=len(a['data']['stem']['remark'])
            for z in range(0,lenth):
                the31mode = (a['data']['stem']['remark'][z]['relation'])
                ans31mod[z]=the31mode
            print(ans31mod)
            lastans=ans31mod
            i = os.system('cls')
            time.sleep(0.01)
        else :
            print(delay)#解决从题库查题时候什么都不显示
            if content == None :
                content = 'null'
            if remark == None :
                remark='null'



                      #隐藏了加密方法




            url = '隐藏了大佬的题库api'
            payload= {"1":1,"1":1,"1":1,"1":"1","1":1}#值以字典的形式传入
            requests.packages.urllib3.disable_warnings()
            response = requests.post(url=url,data=payload,verify=False)
            zidian=json.loads(response.text)
            ans = (zidian['data'])
            i = os.system('cls')#解决从题库查题时候什么都不显示
            print(ans)
            lastans=ans#把答案存在全局变量中 实现一会做错题出问题的时候显示上一个题的答案
            delay=ans #解决从题库查题时候什么都不显示
            if topic_mode == 51 or topic_mode == 52 or topic_mode == 53 or topic_mode == 54:
                pyperclip.copy(zidian['data'])#复制答案到剪贴板
                print(ans)
                print('答案已经自动复制到剪切板啦，直接ctrl+v粘贴就好啦')
                lastans=ans
            time.sleep(1)
            i = os.system('cls')
    else :
        i = os.system('cls')
        print('好像有什么问题，别乱选啊，在做个题试试。')
        print('刚才的答案是')
        print(lastans)
        time.sleep(1)







