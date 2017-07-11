import urllib
import urllib2

page = 1
url = 'http://www.qiushibaike.com/hot/page/'+ str(page)

#if __name__ == '__main__':
try:
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    print response.read()
except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason


