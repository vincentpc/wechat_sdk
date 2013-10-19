# encoding: utf-8

# author hzlzh
# must be python 2.x

import json
import urllib
import urllib2

appid = "c05988627383467d87272456e5ae8b45"
secret = "36f21ca8841e49488240b0a82c5f7ee8"
access_url = "https://api.yixin.im/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s"
menu_url = "https://api.yixin.im/cgi-bin/menu/create?%s"
get_menu_url = "https://api.yixin.im/cgi-bin/menu/get?%s"

def get_access_token():
    f = urllib.urlopen(access_url % (appid, secret))
    resp = json.loads(f.read())
    return resp['access_token']


def generate_menu(token):
    menus = {
        "button": [
            {
                "type": "click",
                "name": "帮助",
                "key": "help"
            },
            {
                "type": "view",
                "name": "关于",
                "url": "about"
            }]
    }
    params = {'access_token': urllib.quote(token)}
    url = menu_url % urllib.urlencode(params)
    print url
    request = urllib2.Request(url, json.dumps(menus, ensure_ascii=False))
    response = urllib2.urlopen(request)
    print response.read()



def get_menu(token):
    params = {'access_token': urllib.quote(token)}
    url = get_menu_url % urllib.urlencode(params)
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    resp = json.loads(response.read())
    print resp
    
def main():
    token = get_access_token()
    #generate_menu(token)
    get_menu(token)

if __name__ == '__main__':
    main()
