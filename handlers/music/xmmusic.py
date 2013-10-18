#-*- coding: UTF-8 -*- 

import urllib
import json

class music:
  def __init__(self):
      self.title = ""
      self.url = ""
      self.description = ""
  
  
class music_api:
  def getsong(songName):
      result = music()
      
      songUrl = 'http://nnlife.duapp.com/xiami.php?key=%s'\
                  % (urllib.quote(songName.encode('utf-8')))#对字符串进行编码
                  
      f = urllib.urlopen(songUrl)
      c = f.read()
      
      data = json.loads(c);
      try:
          if data['status'] == 'ok':
            result.title = data['song']['song_name']
            result.url = data['song']['song_location']
            result.description = data['song']['artist_name']
            return result
          else:
            return None
      except Exception:
          return None
