Crawler of BBS
===

* execute programe:python SpiderStart.py
* program statement:
	+ this program will get all the posts on the WuHan university's bbs in one year.
	+ all the related information will be saved in bbs_db.txt.Of course ,if you want to save them on you own database(mysql only),you can cancel the comment in parser.py(I act as if you know which comment to cancel).
	and I am sorry for not stating enough comment cause of my finite time.
* file function:
	+ save_into_db.py:supply with the db tables' object and the method to operator it.
	+ get_post.py:get all the post on the page according to the the post page's source code and get the next_page url
	+ spider.py:spider function to get the page's source code according to the page's url
	+ parser.py:anylist the page content
	+ SpiderStart.py:the main programe
* extra lib:
	+ urllib2:get the page's source code
	+ SGMLLister:analist the soruce code
	+ MySQLdb:operate the db

