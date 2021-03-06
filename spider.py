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
        self.f = None
    
    #from index page to get the border name 
    def getIndexPageBoardName(self):
        try:
            board_link = urllib2.urlopen(bbs_index_url)
       	except URLError as e:
       	    print e.reason
       	if board_link.code == 200:
			board_parser = bbs_index_parser()
			board_parser.feed(board_link.read())
			for item in board_parser.content:
			    print item
			    if item.find('boards[boards.length]') != -1:
					temp_board_name = item.split('(')[1].split(',')[0]
					board_name = item.split('\'')
					if temp_board_name == '0' :
					    self.board_name_e.append(board_name[1])
					    self.board_name_c.append(board_name[3])
					#deal with the second page
	                else:
	                    borderName = board_name[1]
                        second_url = "http://bbs.whu.edu.cn/wForum/board.php?name="+borderName
                        url_link = urllib2.urlopen(second_url)
                        second_url_parser = bbs_index_parser()
                        second_url_parser.feed(url_link.read())
                        for items in second_url_parser.content:
                            if items.find('boards[boards.length]') != -1:
                                board_name = item.split('\'')
                                self.board_name_e.append(board_name[1])
                                                        
    def start(self):
    	#first get the all boardname of index page
       	self.getIndexPageBoardName()
       	#second form new url just like
       	# bbs.whu.edu.cn/wForum/board.php?name=border_name_e[i]
       	id_parser = bbs_id_parser()
       	post_parser = bbs_parser()
        self.f = open('bbs_db.txt','w')
       	
       	#save into db
       	'''
       	self.bbs_db = bbsDB()
        self.bbs_db.link_db()
        self.post_db = Post()
        self.poster_db = Poster()
        self.pp_relate = post_poster_relation()
        self.bbs_db.select_dbs('bbs_db')
       	'''
       	for item in self.board_name_e:
       	    base_url = 'http://bbs.whu.edu.cn/wForum/board.php?name=' + item + '&page='
       	    page_num = 1
       	    temp_url = base_url + str(page_num)
       	    is_legal = True
       	    print temp_url
       	    while is_legal and page_num < 5:
				try:
				    url_link = urllib2.urlopen(temp_url)
				except URLError as e:
				    print e.reason
				page_num += 1
				temp_url = base_url + str(page_num)
				if url_link.code == 200:
				    url_content = url_link.read()
				    url_content = url_content.decode('gbk','ignore').encode('utf-8')
				    id_parser.feed(url_content)
				    for items in id_parser.content:
				        if items.find('origin = ') != -1:
				    	    tmp = items.split('(')[1]
				    	    #print tmp
				    	    tp = tmp.split(',')
				    	    self.deal_with(item,tp[0],post_parser)
				    	    post_parser = bbs_parser()
				    id_parser = bbs_id_parser()
	    
	    #self.f.close()
	    '''save into db
        self.bbs_db.conn.close()
        '''
       	#third get all the post's id
    def deal_with(self,borderName,ids,post_parser):
        self.f.write('url :')
        new_url = 'http://bbs.whu.edu.cn/wForum/disparticle.php?boardName='+borderName+'&ID='+ids+'&page=1'
        self.f.write(new_url)
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
                    self.f.write('ID:\r:')
                    self.f.write(item[0])
                    self.f.write('\n')
                    self.f.write('name:\r')
                    self.f.write(item[1])
                    self.f.write('\n')
                    self.f.write('Title:\r')
                    self.f.write(item[2])
                    self.f.write(item[3])
                    self.f.write('\n')
                    
                    self.f.write('Content:\r')
                    for items in item[4]:
                        self.f.write(items)
                        self.f.write('\n')
                    self.f.write('Time:\r')
                    self.f.write(item[5])
                    self.f.write('\n\n')
                    
                    '''
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
                    '''
                new_url = ""
                for strs in post_parser.next_url:
                    if strs:
                        new_url = strs
                        break
                print "        ",new_url
                post_parser.set_url()
                if not new_url:
                    is_target = False
                post_parser.set_target()
        return 1
        pass
#for url in parser.urls:
#    print url
