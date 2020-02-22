# -*- coding: utf-8 -
'''
Created on Sun Jan 19 19:48:35 20

@author: 27879
'''

import requests
import md5sign

def get_content(plus_item):
    url = "https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat"
   #get prameters
    plus_item = plus_item.encode('utf-8')
    payload = md5sign.get_params(plus_item)
    # r = requests.get(url,params=payload)
    r = requests.post(url,data=payload)
    return r.json()["data"]["answer"]

#if __name__ == '__main__':
#    while True:
#        comment = input('I：')
#        if comment == 'quit()':
#            break
#        answer=get_content(comment)
#        print('Resp：'+answer)
        
def ask(question):
    comment = question

    answer=get_content(comment)
    return answer