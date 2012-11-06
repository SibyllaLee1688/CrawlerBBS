file_name = ['save_into_db.py','parser.py','spider.py','get_post.py','SpiderStart.py']

st = 0
for item in file_name:
	temp = open(item,'r')
	for tt in temp:
		st += 1

print st
