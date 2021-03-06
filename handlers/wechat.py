from hashlib import sha1
from setting.settings import WECHATTOKEN
import xml.etree.ElementTree as ET
import wechat_xml
import time


class WeChat(object):

    def __init__(self, messageXML):

        root = ET.fromstring(messageXML)
            
        for child in root:
            setattr(self, child.tag, child.text)


    def textResp(self, content, funcflag=0):

        response = wechat_xml.textResp % (
                        self.FromUserName,
                        self.ToUserName,
                        time.time(),
                        content,
                        funcflag
            )


        return response

     
    def musicResp(self, title, description, url,hqurl, funcflag=0):
         response = wechat_xml.musicResp % (
                        self.FromUserName,
                        self.ToUserName,
                        time.time(),
                        title,
                        description,
                        url,
                        hqurl,
                        funcflag
            )
         return response

    @staticmethod
    def make_pic(title, description , picUrl, url):

        item = wechat_xml.picItem % (
                        title,
                        description,
                        picUrl,
                        url
            )

        return item


    def picResp(self, itemList, content='', funcflag=0):
        if itemList == []:
            raise Exception("item list is empty!")

        articleCount = len(itemList)

        if articleCount > 10:
            raise Exception("the number of items can't more than 10")

        picInfo = ''.join(itemList)

        response = wechat_xml.picResp % (
                self.FromUserName,
                self.ToUserName,
                time.time(),
                content,
                articleCount,
                picInfo,
                funcflag,
            )
            
        return response


    @staticmethod
    def valid(signature=None, timestamp=None, nonce=None):
        li = []

        li.append(WECHATTOKEN)
        li.append(nonce)
        li.append(timestamp)

        li.sort()

        tmpWord = ''.join(li)
        tmpWord = sha1(tmpWord).hexdigest()


        if tmpWord == signature:
            return True
        else:
            return False
        
