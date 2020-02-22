# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 15:12:56 2020

@author: Showi


QQ chatbot
"""

import get1
import Send
#from robot import ask
import time
from robot02 import ask
#to_who = input('选一个群:')#要提前设定发给谁
to_who = input('开始,输入目标群组:')
#yourname = input('你的群备注:')
yourname = '小冰'
#li = []
while(True):
    mesList = get1.getMes()#获取了消息
    for i in mesList:
        print('#',i)
#        print(li)
#        if i in li:
#            continue
        print('#',('@'+yourname) not in i)
        isInside = '@'+yourname
        #isInside = '/'
        if isInside not in i:
            continue
        i = i.split(isInside)[1]
        responseMes = ask(i)
#        li.append(responseMes)
        print('#',responseMes)
        Send.send_qq(to_who,responseMes)
    time.sleep(1)

    
    
    
