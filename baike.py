# -*- coding: utf-8 -*-
import urllib
import urllib2

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)


def handle():
    class myClass(object):
        def __init__(self):    #对各种基本数据类型测试
            self.x = []        #列表
            self.y = None         #数值
            self.z = {}        #字典
            self.a = str()     #字符串


        def _handle(self):
            self.x.append('hello', 'world')
            self.y = 1
            self.z['hello'] = 'world'
            self.a = "".join("hello")


    my_class = myClass()

    return my_class.x, my_class.y, my_class.z, my_class.a
    pass

if __name__ == '__main__':
    '''try:
        request = urllib2.Request(url)
        for item in request.header_items():
            print item
        response = urllib2.urlopen(request)
        print response.read()
    except urllib2.URLError, e:
        if hasattr(e, "code"):
            print e.code
        if hasattr(e, "reason"):
            print e.reason'''


    my_x, my_y, my_z, my_a = handle()
    pass








