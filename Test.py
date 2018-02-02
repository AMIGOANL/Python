# -*- coding: utf-8 -*-
# print 'Hello,World!'
# 
# print 'The quick brown fox','jumps over','the lazy dog'
# 
# print '100 + 200 =',100 + 200
# raw_input返回的一定是字符串
# name = raw_input('Please enter your name:')
# print 'Hello,',name
# 
# print r'\\\n\\'
# 
# print '\\\n\\'
# 

# print '''line1
# line2
# line3'''
# print u'浩浩SAMA'
# 
# list
# list元素的数据类型可以为不同
# 其元素也可以为另一个list，但元素还是那么多，如s依旧只有两个元素
# classmates = ['Michael','Bob','Tracy']
# s = ['AMIGOANL',classmates]
# print classmates,len(classmates),classmates[0],classmates[-1]
# 末尾加
# classmates.append('Adam')
# 定位加
# classmates.insert(1,'Jack')
# 末尾删
# classmates.pop()
# # 定位删
# classmates.pop(1)
# 定位替换
# classmates[1] = 'Sarah'
# print s
# 
# 
# tuple
# 元素固定，不可增删且无法赋值成另外元素，和list相比最大的优势就是“安全”
# 但定义一个元素的tuple时，在元素后加‘，’，防止引发歧义
# 
# 
# age = 16
# if age >= 18:
#  	print 'your age is %s,and you are a adult' % age 
# else:
# 	print 'you are a teenager'
# 	
# 	
# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
# if x:
# 	print 'True'
# 	
# for x in ...循环就是把每个元素代入变量x，然后执行缩进块的语句。	
# names = ['A','B','C']
# for name in names:
# 	print name
# 	
# sum = 0
# for x in [1,2,3,4,5,6,7,8,9,10]:
# 	sum = sum + x
# print sum
# 0-100
# sum = 0
# for x in range(101):
# 	sum = sum + x
# print sum
# 
# 
# dict 字典，相当于java中的Map
# key若不存在，dict就会报错，为了避免这种情况，有两种方法
# 1.通过in 2.通过get方法
# d = {'Michael':95,'Bob':75,'Tracy':85}
# d['Adam'] = 67
# d['Adam'] = 85
# d.pop(Bob)
# # d['AMIGOANL']
# print d['Adam']
# print'AMIGOANL' in d
# print d.get('AMIGOANL',-1)
# 
# 
# set和dict类似，也是一组key的集团，但不储存value，使用remove删除元素
# s1 = set([1,2,3])
# s2 = set([2,3,4])
# print s1 & s2
# print s1 | s2
# 
# print 4687*(6.75/6.33)
# print 7.6/7.1
# 

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('www.sina.com.cn',80))
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
buffer = []
while True:
	d = s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break
data = b''.join(buffer)

s.close()

header,html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
with open('sina.html', 'wb') as f:
	f.write(html)