#-*- coding: UTF-8 -*- 

import urllib
import re
import platform


def getSongUrl(songName,authorName):
    '''这里由于歌曲名称和作者名称的不完整，可能导致无法得到url，'''
    songUrl = 'http://box.zhangmen.baidu.com/x?op=12&count=1&title=%s$$%s$$$$'\
                % (urllib.quote(songName.encode('gbk')),urllib.quote(authorName.encode('gbk')))#对字符串进行编码
    f = urllib.urlopen(songUrl)
    c = f.read()
    url1 = re.findall('<encode>.*?CDATA\[(.*?)\]].*?</encode>',c)
    url2 = re.findall('<decode>.*?CDATA\[(.*?)\]].*?</decode>',c)
    if len(url1) <1:
        return 'http://box.zhangmen.baidu.com/unknow.mp3'
    
    try:
        return url1[0][:url1[0].rindex('/')+1] + url2[0]
    except Exception:
        return url1[0]
