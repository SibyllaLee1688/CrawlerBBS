# -*- coding: utf-8 -*-
from parser import *
import urllib2
from urllib2 import URLError
import errno
from get_post import get_post
from save_into_db import *
bbs_index_url = 'http://bbs.whu.edu.cn/wForum/index.php'

#the spider engine for sina blog

    
    
class BbsSpider:
    def __init__(self ,link):
        self.link = link
        self.board_name_e = []#engine
        self.board_name_c = []#chinese
        self.board_urls = []
    	self.post_id = []
        self.bbs_db = None
        self.post_db = None
        self.poster_db = None
        self.pp_relate = None
    
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
	
				
    def start(self):
    	#first get the all boardname of index page
       	self.getIndexPageBoardName()
       	#second form new url just like
       	# bbs.whu.edu.cn/wForum/board.php?name=border_name_e[i]
       	f = open("1.txt","w")
       	id_parser = bbs_id_parser()
       	post_parser = bbs_parser()
       	self.bbs_db = bbsDB()
        self.bbs_db.link_db()
        self.post_db = Post()
        self.poster_db = Poster()
        self.pp_relate = post_poster_relation()
        self.bbs_db.select_dbs('bbs_db')
       	for item in self.board_name_e[0:1]:
       	    temp_url = 'http://bbs.whu.edu.cn/wForum/board.php?name=' + item + '&page=1'
       	    is_legal = True
       	    print temp_url
       	    while is_legal:
				try:
				    url_link = urllib2.urlopen(temp_url)
				except URLError as e:
				    print e.reason
				if url_link.code == 200:
				    url_content = url_link.read()
				    url_content = url_content.decode('gbk','ignore').encode('utf-8')
				    id_parser.feed(url_content)
				    temp_url = ""
				    for urls in id_parser.next_url:
				        if urls:
				            temp_url = urls
				            break
				    id_parser.set_url()
				    if not temp_url:
				        is_legal = False
				        continue
				    for items in id_parser.content:
				        if items.find('origin = ') != -1:
				    	    tmp = items.split('(')[1]
				    	    #print tmp
				    	    tp = tmp.split(',')
				    	    if not self.deal_with(item,tp[0],post_parser):
				    	        is_legal = False
				    	        break
				    	    
				    	    f.write(tp[0])
				    	    f.write('\n')
				    id_parser.content = []
        self.bbs_db.conn.close()
       	#third get all the post's id
    def deal_with(self,borderName,ids,post_parser):
        new_url = 'http://bbs.whu.edu.cn/wForum/disparticle.php?boardName='+borderName+'&ID='+ids+'&page=1'
        print "    " + new_url
        #print type(new_url)
        next_url = new_url
        is_target = True
        while is_target and next_url:
            try:
                link_content = urllib2.urlopen(new_url)
            except URLError as e:
                print e.reason
                continue
            
            if link_content.code == 200:
                html = link_content.read()
                html = html.decode('gbk','ignore').encode('utf-8')
                #print html
                st = get_post(html,post_parser)
                
                for item in st:
                    #print item
                    self.post_db.set_value(item[0],item[5],item[2],item[4])
                    self.post_db.insert_value(self.bbs_db.cursor)
                    self.bbs_db.conn.commit()
                    self.poster_db.set_value(item[0],item[1])
                    self.poster_db.insert_value(self.bbs_db.cursor)
                    self.bbs_db.conn.commit()
                    
                    poster_id = self.poster_db.get_id(item[0],self.bbs_db.cursor)
                    post_id = self.post_db.get_id(item[0],item[5],self.bbs_db.cursor)
                    #print poster_id,post_id
                    self.bbs_db.conn.commit()
                    self.pp_relate.set_value(post_id,poster_id,item[3])
                    self.pp_relate.insert_value(self.bbs_db.cursor)
                    self.bbs_db.conn.commit()
                
                new_url = ""
                for strs in post_parser.next_url:
                    if strs:
                        new_url = strs
                        break
                print new_url
                post_parser.set_url()
                if not new_url:
                    is_target = False
                if not post_parser.is_target:
                    return 0
                post_parser.set_target()
        return 1
        pass
#for url in parser.urls:
#    print url
