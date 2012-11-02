#-*- coding: utf-8 -*-
from spider import *

f = open("1.txt","w")
searchContent = raw_input()
link = "http://bbs.whu.edu.cn/wForum/index.php"
#link = "http://bbs.whu.edu.cn/wmainpage.php"
#link = "http://bbs.whu.edu.cn/wForum/disparticle.php?boardName=Digital"
#link = "http://bbs.whu.edu.cn/wForum/frames.php?target=../wmainpage.php"
#link = "http://bbs.whu.edu.cn/wForum/frames.php"
#print link

spiderE = BbsSpider(link)
spiderE.start()

#for url in parser.urls:
#    print url

