
# -*- coding: utf-8 -*-
import urllib2
from sgmllib import SGMLParser
import re
        
# spider engine to get all the link of a target link
dic = {}

#the spider engine for sina blog
class bbs_parser(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.url = []
        self.is_td = False
        self.is_just = False
        self.is_target = True
        self.next_url = []
    def start_td(self,attrs):
        href = [v for k,v in attrs if k == 'class' or k == 'width']
        if len(href) == 2 and href[0].find('TableBody') != -1 and href[1] == '*':
            self.is_td = True
        elif len(href) == 2 and href[0].find('TableBody') != -1 and href[1] == "175":
            self.is_td = False
            
    def start_a(self,attrs):
	    head_url = ""
	    if (len(attrs) == 2 and attrs[0][0] == 'href' and attrs[1][1] == '下一页'):
	        head_url = 'http://bbs.whu.edu.cn/wForum/'
	        #print 'hellllllo'
	        head_url += attrs[0][1]
            self.next_url.append(head_url)
    def set_url(self):
        self.next_url = []
          
    def handle_data(self,attrs):
        if self.is_td and attrs != " ":
            self.url.append(attrs)
            self.is_just = True
        if attrs.find('guest用户暂无权限阅读') != -1:
            print 'error'
            self.is_target = False
        
    def set_target(self):
        self.is_target = True
        
    def start_br(self,attrs):
        if self.is_just:
            self.url.append('\n')
            self.is_just = False

#the spider to get all the boardName in bbs.whu.edu.cn/wForum/index.php
class bbs_index_parser(SGMLParser):
	def reset(self):
		SGMLParser.reset(self)
		self.boardName = []
		self.content = []
		
	def handle_comment(self,attrs):
		if attrs.find('boards') != -1:
			st = attrs.split('\n')#split the string
			for item in st:
				self.content.append(item)
				
#the spider to get all the context's id in bbs.whu.edu.cn/wForum/board.php?name=*
class bbs_id_parser(SGMLParser):
	def reset(self):
		SGMLParser.reset(self)
		self.content = []
		self.next_url = []
	    
	    
	    
	def start_a(self,attrs):
	    head_url = ""
	    if (len(attrs) == 2 and attrs[0][0] == 'href' and attrs[1][1] == '下一页'):
	        head_url = 'http://bbs.whu.edu.cn/wForum/'
	        head_url += attrs[0][1]
            self.next_url.append(head_url)
	
	def set_url(self):
	    self.next_url = []
	
	def handle_comment(self, attrs):
		if attrs.find('boardName') != -1:
			st = attrs.split('\n')
			for item in st:
			    self.content.append(item)
        pass
    
    
