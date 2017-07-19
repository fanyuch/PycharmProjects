# -*- coding: utf-8 -*-

import requests
from PIL import Image
import HTMLParser

class doubanClitne(object):
    def __init__(self):
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
        self.session = requests.session()

    def login(self,
              username,
              password,
              login=u"登陆",
              source="index_nav",
              redir="https://www.douban.com/"):

        data = {"form_email": username,
                "form_password": password,
                "source": source,
                "redir": redir,
                "login": login,
                }

        login_url = "https://accounts.douban.com/login"
        respone = self.session.get(login_url)


        (captcha_id, captcha_url) = prepCaptcha(respone.content)

        if captcha_id:
            r = self.session.get(captcha_url)
            with open("captcha_image", "wb") as f:
                f.write(r.content)
            try:
                im = Image.open("captcha_image")
                im.show()
                im.close()
            except Exception, e:
                print e.message
            captcha_solution = raw_input("please input solution for captcha [{}]".format(captcha_url))
            data["captcha-id"] = captcha_id
            data["captcha-solution"] = captcha_solution

        try:
            self.session.post(login_url, data=data, headers=self.headers)
        except Exception, e:
            print e.message
        pass

        print self.session.get("https://www.douban.com").content


def prepCaptcha(content):
    class captchaParser(HTMLParser):
        def __init__(self):
            HTMLParser.__init__(self)
            self.captcha_id = None
            self.captcha_url = None

        def _attr(attrs, attrname):
            for i in attrs:
                if i[0] == attrname:
                    return i[1]
            return None

        def handle_strattag(self, tag, attr):
            if tag =='img' and \
                            self._attrs(attr, 'id') == 'captcha_image' and \
                            self._attrs(attr, 'class') =='captcha_image':
                self.captcha_url = self._attrs(attr, 'src')

            if tag == 'input' and \
                    self._attrs(attr, 'type') == 'hidden' and \
                self._attrs(attr, 'name') == 'captcha-id':
                self.captcha_id = self._attrs(attr, 'value')

    myCapt = captchaParser()
    myCapt.feed()

    return myCapt.captcha_url, myCapt.captcha_id








if __name__ == '__main__':
    username = raw_input("请输入用户名")
    password = raw_input("请输入密码")
    myDoban = doubanClitne()
    myDoban.login(username=username, password=password)
    pass
