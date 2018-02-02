import urllib2
import urllib
import cookielib
# response = urllib2.urlopen("http://www.baidu.com")
# print response.read()


# POST
# values = {}
# values['username'] = "980921032@qq.com"
# values['password'] = "AMIGO960108"
# 
# values = {"username":"980921032@qq.com","password":"AMIGO960108"}
# data = urllib.urlencode(values)
# url = "https://mail.qq.com/"
# request = urllib2.Request(url,data)
# response = urllib2.urlopen(request)
# print response.read()


# # GET
# values = {"username":"XXX","password":"XXX"}
# data = urllib.urlencode(values)
# url = "https://mail.qq.com/"
# geturl = url + "?" + data
# request = urllib2.Request(geturl)
# response = urllib2.urlopen(request)
# print response.read
# 
# 
# 
filename = 'test.txt'
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({'stuid':'XXXXX','pwd':'XXX'})
loginUrl = 'XXXXXXXXXX'
result = opener.open(loginUrl,postdata)
cookie.save(ignore_discard=True,ignore_expires=True)
gradeUrl = 'XXXXX'
result = opener.open(gradeUrl)
print result.read()