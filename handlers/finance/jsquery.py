#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2

def queryAny(codelist):
    clist = ['f_%s' % c for c in codelist]
    url = 'http://hq.sinajs.cn/list=%s' % ','.join(clist)
    response = urllib2.urlopen(url)
    var = response.read()
    vlist = var.split('";\n')
    result = list()
    for v in vlist:
        if v:
            v1 = v.split('="')
            v2 = v1[1].split(',')
            cdict = dict(code=v1[0][13:], name=v2[0].decode('gb2312'),
                        newnet=v2[1],
                        daygrowrate=('%.2f%%' % ( 100*(float(v2[1])-float(v2[3]))/float(v2[3]) )))
            result.append(cdict)
    return result

def query_fund(code):
    url = 'http://hq.sinajs.cn/list=f_%s' % code
    response = urllib2.urlopen(url)
    var = response.read()
    v = var[:-3]
    v1 = v.split('="')
    if not v1[1]:
        return None
    else:
        v2 = v1[1].split(',')
        return dict(code=v1[0][13:], name=v2[0].decode('gb2312'),
                   newnet=v2[1],
                   daygrowrate=('%.2f%%' % ( 100*(float(v2[1])-float(v2[3]))/float(v2[3]) )))

def query_stock(code,type):
    if type == 1:
        url = 'http://hq.sinajs.cn/list=sh%s' % code
    elif type == 0:
        url = 'http://hq.sinajs.cn/list=sz%s' % code
    else:
        return None
    response = urllib2.urlopen(url)
    var = response.read()
    v = var[:-3]
    v1 = v.split('="')
    if not v1[1]:
        return None
    else:
        v2 = v1[1].split(',')
        return dict(code=v1[0][13:], name=v2[0].decode('gb2312'),open=v2[1],\
                nowprice=v2[3],\
                daygrowrate=('%.2f%%' % ( 100*(float(v2[3])-float(v2[2]))/float(v2[2]) )))


def queryReal(codelist):
    clist = ['fu_%s' % c for c in codelist]
    url = 'http://hq.sinajs.cn/list=%s' % ','.join(clist)
    response = urllib2.urlopen(url)
    var = response.read()
    vlist = var.split('";\n')
    result = list()
    for v in vlist:
        if v:
            v1 = v.split('="')
            if v1[1]:
                v2 = v1[1].split(',')
                cdict = dict(code=v1[0][14:], name=v2[0].decode('gb2312'),
                            newnet=v2[2],
                            daygrowrate=('%.2f%%' % float(v2[6])))
                result.append(cdict)
            else:
                pass
    return result

