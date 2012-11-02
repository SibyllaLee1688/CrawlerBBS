# -*- coding: utf-8 -*-
from crawler import bbs_spider
import urllib2
bbs_url = 'bbs.whu.edu.cn'

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

class BbsSpider:
    def __init__(self ,link):
        self.link = link
    
    def start(self):
        '''        header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.121 Safari/535.2',\
                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',\
                'Accept-Charset':'GBK,utf-8;q=0.7,*;q=0.3',\
                'Accept-Language':'zh-CN,zh;q=0.8',\
                'Accept-Encoding':'gzip,deflate,sdch'}
        '''        

        #eq = urllib2.Request(self.link,'',header) 
        linkContent = urllib2.urlopen(self.link)
        
        if linkContent.code == 200:
            print 'ni'
            parser = bbs_spider()
            parser.feed(linkContent.read())
            print parser.url
            for st in range(0 ,len(parser.url) - 1):
                print parser.url[st]
            linkContent.close()
            

#for url in parser.urls:
#    print url

