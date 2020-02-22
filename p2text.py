# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 14:20:02 2020

@author: Showi
"""

# encoding:utf-8

import requests
import base64
import os

'''
通用文字识别
'''

def p2text(imgPath):
    '''将图片转换为文字'''
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"
    # 二进制方式打开图片文件
    f = open(imgPath, 'rb')
    img = base64.b64encode(f.read())
    f.close()
    params = {"image":img}
    ##################################################################################
    access_token = '[find the access_token on https://ai.baidu.com/tech/ocr/general]'
    ##################################################################################
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print('||',response.json())
        recMes = (response.json())['words_result']
        recMesText = []
        for one in recMes:
            recMesText.append(one['words'])
        os.remove(imgPath)#删除垃圾
        return(recMesText)