
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import urllib2
import re
import sys
from sgmllib import SGMLParser
from parser import bbs_parser
# spider engine to get all the link of a target link
Dic = {}
def get_post(html,st):
    final = []
    f = open("2.txt","w")
    st.feed(html)
    page = 1
    is_lou = 0
    is_end = False
    poster_e = ""
    poster_c = ""
    poster_title = ""
    poster_time = ""
    poster_content = []
    final = []
    is_start = False
    sts = ""
    fn = [] 
    for item in st.url:
        if page == 1:
            if item != '\n':
                sts = sts + item
            else:
                final.append(sts)
                sts = ""

    for item in final:
        ans = ""
        tp = item.split("\r\n")
        for st in tp:
            if st:
               ans = st
        fn.append(ans)
    final = []
    tf = open("3.txt","w")
    is_post_end = False
    for item in fn:
        temp = []
        tf.write(item)
        tf.write('\n')
        if item.find("发信人") == 0 and not is_start:
            name = item.split(":")[1].split("(")
            poster_e = name[0]
            is_start = False
            is_end = False
            poster_c = name[1].split(")")[0]
        elif item.find(' 标 题:') == 0 and not is_start:
            poster_title = item.split("标 题:")[1]
            if poster_title.find(' Re:') == 0:
                is_re = 1
            else:
                is_lou = 1
        elif item.find(' 发信站: 珞珈山水') == 0:
            poster_time = item.split('(')[1].split(')')[0]
            is_start = True
        elif item.find(' --') == 0:
            is_end = True
            is_start = False
        else:
            if item.find("※ 来源") == -1  and not is_end and is_start:
                poster_content.append(item)
            elif item.find("※ 来源") != -1:
                is_end = False
                is_start = False
                temp.append(poster_e)
                temp.append(poster_c)
                temp.append(poster_title)
                temp.append(str(is_lou))
                temp.append(poster_content)
                temp.append(poster_time)
                final.append(temp)
                f.write('ID:\r')
                f.write(poster_e)
                f.write('\n')
                f.write('name\r')
                f.write(poster_c)
                f.write('\nTitle:\r')
                f.write(poster_title)
                f.write(str(is_lou))
                f.write('\nContent:\r')
                for each in poster_content:
                    f.write(each)
                    f.write('\n\r')
                f.write('time:\r')
                f.write(poster_time)
                f.write('\n\n')
                is_lou = 0
                poster_c = ""
                poster_e = ""
                poster_title = ""
                poster_content = []
                poster_time = ""
    return final



