# -*- coding:utf-8 -*-

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
        elif t.startswith("stocksh"):
            data = query_stock(t[8:],1)
            if data:
                text = u"%s\nreal price: %s\ngrowth: %s" %\
                    (data['name'], data['nowprice'], data['daygrowrate'])
            else:
                text = u"stock not exist"
        elif t.startswith("stocksz"):
            data = query_stock(t[8:],0)
            if data:
                text = u"%s\nreal price: %s\ngrowth: %s" %\
                     (data['name'], data['nowprice'], data['daygrowrate'])
            else:
                text = u"stock not exist"


        elif t.startswith('test'):
            data = t[5:]
            text = u"echo back: %s\n" % (data) #echo back
        else:
            text = help
        
        response = wechat.textResp(content = text, funcflag = 0)
    else:
        text = help
    

    return response
    
