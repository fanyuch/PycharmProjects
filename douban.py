# -*- coding: utf-8 -*-

import requests
import getpass

class doubanClitne(object):
    def __init__(self):
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
        self.session = requests.session()

    def login(self,
              username,
              password,
              login=u"登陆",
              source="index_nav",
              redir="https://www.douban.com/"):
        login_url = "https://accounts.douban.com/login"
        respone = self.session.get(login_url)
        data = {"form_email":username,
                "form_password":password,
                "source":source,
                "redir":redir,
                "login":login}
        self.session.post(login_url, data = data, headers = self.headers)
        print self.session.get("https://www.douban.com").content


if __name__ == '__main__':
    username = raw_input("请输入用户名")
    password = getpass.getpass("请输入密码")
    myDoban = doubanClitne()
    myDoban.login(username=username, password=password)
    input("hello")
