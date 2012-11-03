
# -*- coding: utf-8 -*-
import urllib2
from sgmllib import SGMLParser
        
# spider engine to get all the link of a target link
dic = {}

#the spider engine for sina blog
class bbs_parser(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.url = []
        
    def start_a(self,attrs):
        href = [v for k,v in attrs if k == 'href']
        if href:
            self.url.append(href)

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
	
	def handle_comment(self, attrs):
		if attrs.find('boardName') != -1:
			st = attrs.split('\n')
			for item in st:
			    self.content.append(item)
	


            
