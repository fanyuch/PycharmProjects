import re
from urllib import parse, request
import http.cookiejar
from PIL import Image
import time
import json

#print(__name__)

cookie = http.cookiejar.LWPCookieJar('cookie')

try:
    cookie.load(ignore_discard=True)
except IOError:
    print('cookie not load')

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36',
           "Host": "www.zhihu.com",
           "Referer": "https://www.zhihu.com/", }

opener = request.build_opener(request.HTTPCookieProcessor(cookie))
opener.addheaders = [(key, value) for key, value in headers.items()]

#if __name__ == '__main__':


def get_xsrf():
    response = opener.open("http://www.zhihu.com")
    html = response.read().decode("utf-8")
    #print(html)
    get_xsrf_pattern = re.compile(r'<input type="hidden" name="_xsrf" value="(.*?)"')
    _xsrf = get_xsrf_pattern.findall(html)
    tmp = _xsrf
    #tmp = re.findall(get_xsrf_pattern, html)
    #tmp1 = tmp
    #_xsrf = re.findall(get_xsrf_pattern, html)[0]
    #get_xsrf_pattern.findall()
    return _xsrf[0]

def get_captcha():
    t = str(int(time.time() * 1000))
    captcha_url = 'http://www.zhihu.com/captcha.gif?r='+t+"&type=login"

    image_data = opener.open(captcha_url).read()
    with open('cptcha.gif', 'wb') as f:
        f.write(image_data)
    im = Image.open('cptcha.gif')
    im.show()
    captcha = input('the code this time is')
    return captcha

def login(username, password):
    if re.match(r'\d{11}$', account):
        url = 'http://www.zhihu.com/login/phone_num'
        data = {
            '_xsrf':get_xsrf(),
            'password':password,
            'remember_me':'true',
            'phone_num':username
        }
    else:
        url = 'http://www.zhihu.com/login/email'
        data = {
            '_xsrf':get_xsrf(),
            'password':password,
            'remember_me':'true',
            'email':username
        }

    post_data = parse.urlencode(data).encode('utf-8')
    r = opener.open(url, post_data)
    result = r.read().decode('utf-8')

    '''x = json.loads(result)
    y = x["r"]
    if (json.loads(result))["r"] == 1:
        data['captcha'] = get_captcha()
        post_data = parse.urlencode(data).encode('utf-8')
        r = opener.open(url, post_data)
        result = r.read().decode('utf-8')
        print((json.loads(result))['msg'])'''

    cookie.save(ignore_discard= True, ignore_expires=True)


def isLogin():
    url = 'https://www.zhihu.com/settings/profile'
    actual_url = opener.open(url).geturl()
    if actual_url == 'https://www.zhihu.com/settings/profile':
        return True
    else:
        return False

if __name__ == '__main__':
    if isLogin():
        print("had logedin")
    else:
        account = input('input account')
        secret = input('input passport')
        login(account, secret)

def printName():
    print(__name__)





