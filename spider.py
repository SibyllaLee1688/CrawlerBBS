# -*- coding: utf-8 -*-
from parser import *
import urllib2
from urllib2 import URLError
import errno
bbs_index_url = 'http://bbs.whu.edu.cn/wForum/index.php'


class post_obj:
	def __init__(self):
		self.id = ''
		self.poster 

def spider_dfs(url):
    is_legal_url = url.find('http://')
    new_url = ''
    if is_legal_url == -1: #the url is relative path
        if url[0] == '\\':
            new_url = bbs_url + url
        else:
            new_url = bbs_url + '\\' + url
    else:
        new_url = url
    
    if new_url.find('bbs.whu.edu.cn') != -1:
        linkContent = urllib2.urlopen(new_url)
        if linkContent.code == 200:
            parser = bbs_spider()
            parser.feed(linkContent.read())
            for item in parser.url:
                spider_dfs(item)
    return

def deal_with(borderName,ids):
    url = 'http://bbs.whu.edu.cn/wForum/disparticle.php?boardName='+borderName+'&ID='+ids+'&page='
    rd = 1
    post_parser = bbs_parser()
    is_target = True
    while is_target and rd < 10:
        new_url = url + str(rd)
        rd += 1
        print new_url
        
        
        try:
            link_content = urllib2.urlopen(new_url)
        except URLError as e:
            print e.reason
            continue
        
        if link_content.code == 200:
            post_parser = bbs_parser()
            post_parser.feed(link_content.read())
        
    pass
    
class BbsSpider:
    def __init__(self ,link):
        self.link = link
        self.board_name_e = []#engine
        self.board_name_c = []#chinese
        self.board_urls = []
    	self.post_id = []
    
    #from index page to get the border name 
    def getIndexPageBoardName(self):
        board_link = urllib2.urlopen(bbs_index_url)
       	if board_link.code == 200:
			board_parser = bbs_index_parser()
			board_parser.feed(board_link.read())
			for item in board_parser.content:
				if item.find('boards[boards.length]') != -1:
					board_name = item.split('\'')
					self.board_name_e.append(board_name[1])
					self.board_name_c.append(board_name[3])
	
	#get all the posts from the url
	def deal(self):
	    pass
	    '''
	    
	    '''
				
    def start(self):
    	#first get the all boardname of index page
       	self.getIndexPageBoardName()
       	#second form new url just like
       	# bbs.whu.edu.cn/wForum/board.php?name=border_name_e[i]
       	f = open("1.txt","w")
       	id_parser = bbs_id_parser()
       	
       	for item in self.board_name_e[0:3]:
			for page_num in range(1,11,1):
				temp_url = 'http://bbs.whu.edu.cn/wForum/board.php?name=' + \
				item + '&page=' + str(page_num)
				
				try:
				    url_link = urllib2.urlopen(temp_url)
				except URLError as e:
				    print e.reason
				if url_link.code == 200:
				    id_parser.feed(url_link.read())
				    for items in id_parser.content:
				        if items.find('origin = ') != -1:
				    	    tmp = items.split('(')[1]
				    	    tp = tmp.split(',')
				    	    #self.post_id.append(tp[0])
				    	    deal_with(item,tp[0])
				    	    f.write(tp[0])
				    	    f.write('\n')
       	#third get all the post's id
       	    
			
#for url in parser.urls:
#    print url
