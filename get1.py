# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 14:20:20 2020

@author: Showi

从屏幕中抓取指定位置的图像
图像转换为文字
通过文字产生输出
叫输出的文字Send

"""

import time
from p2text import p2text
from PIL import ImageGrab, Image
folderpath = 'images'

# 区域截图left, upper, right, lower
def screenRegion():
    '''调用此函数，然后返回截屏的位置'''
    try:
        left, top = 10, 720
        width, height = 500, 667/6 - 20  # iphone6
        bbox = (left, top, left + width, top + height)
        img = ImageGrab.grab(bbox)
        newfilename = "images/{}{}.jpg".format(folderpath,int(time.time() * 1000))
        img.save(newfilename)
        #    img.show()
        print("screen saved!")
    except Exception as e:
        print('error')
        print("error:",e)
    finally:
        return newfilename
  

def getMes():
    '''得到最近发的消息，返回一个字符串列表'''
    imgPath = screenRegion()
    textList = p2text(imgPath)
    return textList

