
# -*- coding: utf-8 -*-
import urllib2
import re
import sys
from sgmllib import SGMLParser
        
# spider engine to get all the link of a target link
Dic = {}

#the spider engine for sina blog
class parser(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.url = []
        self.is_td = False
        self.is_just = False
        
    def start_td(self,attrs):
        href = [v for k,v in attrs if k == 'class' or k == 'width']
        if len(href) == 2 and href[0].find('TableBody') != -1 and href[1] == '*':
            self.is_td = True
        elif len(href) == 2 and href[0].find('TableBody') != -1 and href[1] == "175":
            self.is_td = False
            
            
    def handle_data(self,attrs):
        if self.is_td and attrs != " ":
            self.url.append(attrs)
            self.is_just = True
            
    def start_br(self,attrs):
        if self.is_just:
            self.url.append('\n')
            self.is_just = False
            
link = urllib2.urlopen("http://bbs.whu.edu.cn/wForum/disparticle.php?boardName=Advice&ID=1105516250&page=1")
html = link.read()
st = parser()
f = open("2.txt","w")
typ = sys.getfilesystemencoding()
st.feed(unicode(html,"GB2312").encode('utf-8'))

print st.url[12].find("发信人")
page = 1
is_lou = 0
is_end = False
poster_e = ""
poster_c = ""
poster_title = []
poster_time = ""
poster_re = []
poster_content = []
for item in st.url:
    if page == 1:
    #    f.write("ID: ")
        #print item.find("楼")
        sts = re.findall(ur'楼主',item) 
        if sts:
            print 'ne'
        
        '''
            is_lou = 1
            is_re = 0
        elif not re.findall(r"第.楼",item):
            is_lou = 0
            is_re = 1
        elif item.find("发信人") != -1:
            st = item.split(":")
            ans = st.split("(")
            poster_e = ans[0]
            poster_c = ans[1].split(")")[0]
        elif item.find("标题:") != -1 and is_lou:
            poster_title.append(tem.split(':')[1])
            
        elif item.find("发信站") != -1:
            poster_time = item.split(":")[1].split("(")[1].split(")")[0]
        elif item.find("--") != -1:
            is_end = True
            
        '''
        '''
        else:
            if not is_end:
                if item.find("大作中提到") != -1 or item.find(":") != -1 and not is_end:
                   poster_re.append(item)
                else:
                    poster_content.append(item)
            elif item.find('来源:') != -1:
                f.write(poster_e)
                f.write('\n')
                f.write("name: ")
                f.write(poster_c)
                f.write('\n')
                for items in poster_content:
                    f.write(items)
                    f.write("\n")
                if is_lou:
                    f.write('title: ')
                    f.write(poster_title)
                    f.write('\n')
                f.write('time: ')
                f.write(poster_time)
                if is_re:
                    f.write('source: ')
                    for items in poster_re:
                        f.write(items)
                        f.write('\n')
                is_lou = False
                is_re = False
                is_end = False
            '''
