#-*- coding: UTF-8 -*- 

import urllib
import json


def getSongUrl(songName,authorName):
    '''这里由于歌曲名称和作者名称的不完整，可能导致无法得到url，'''
    songUrl = 'http://api2.sinaapp.com/search/music/?appkey=0020130430&appsecert=fa6095e1133d28ad&reqtype=music&keyword=%s'\
                % (urllib.quote(songName.encode('utf-8')))#对字符串进行编码
                
    f = urllib.urlopen(songUrl)
    c = f.read()
    
    data = json.loads(c);
    try:
        if data['errcode'] == 0:
          return data['music']['musicurl']
        else:
          return ""
    except Exception:
        return ""
