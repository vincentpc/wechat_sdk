# -*- coding:utf-8 -*-

import logging

from search.gsearch import GoogleAPI
from finance.jsquery import query_fund,query_stock
from handlers.wechat import WeChat
import setting.settings as settings


def processXml(xml):
    wechat = WeChat(xml)
    help = settings.HELP

    if wechat.MsgType  == 'event':
            return None
    elif wechat.MsgType == 'text':
        t = wechat.Content
        if t.startswith("fund"):
            data = query_fund(t[5:])
            if data:
                text = u"%s\nnet value: %s\ngrowth: %s" %\
                        (data['name'], data['newnet'], data['daygrowrate'])
            else:
                text = u"fund not exist"
            response = wechat.textResp(content = text, funcflag = 0)
        elif t.startswith("stocksh"):
            data = query_stock(t[8:],1)
            if data:
                text = u"%s\nreal price: %s\ngrowth: %s" %\
                    (data['name'], data['nowprice'], data['daygrowrate'])
            else:
                text = u"stock not exist"
            response = wechat.textResp(content = text, funcflag = 0)
        elif t.startswith("stocksz"):
            data = query_stock(t[8:],0)
            if data:
                text = u"%s\nreal price: %s\ngrowth: %s" %\
                     (data['name'], data['nowprice'], data['daygrowrate'])
            else:
                text = u"stock not exist"
            response = wechat.textResp(content = text, funcflag = 0)
        elif t.startswith('google'):
            query = t[7:]
            api = GoogleAPI()
            result = api.search(query)
            itemlist = []
            for r in result:
                pic_item = wechat.make_pic(r.getTitle(),\
                        r.getContent(),"",r.getURL())
                itemlist.append(pic_item)
            response = wechat.picResp(itemlist,funcflag = 0)

        elif t.startswith('test'):
            data = t[5:]
            text = u"echo back: %s\n" % (data) #echo back
            response = wechat.textResp(content = text, funcflag = 0)
        else:
            text = help
            response = wechat.textResp(content = text, funcflag = 0)
    else:
        text = help
        response = wechat.textResp(content = text, funcflag = 0)

    return response
    
