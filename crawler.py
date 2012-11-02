
# -*- coding: utf-8 -*-
import urllib2
from sgmllib import SGMLParser
        
# spider engine to get all the link of a target link
dic = {}

#the spider engine for sina blog
class bbs_spider(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.url = []
        
    def start_a(self,attrs):
        href = [v for k,v in attrs if k == 'href']
        if href:
            self.url.append(href)
            
