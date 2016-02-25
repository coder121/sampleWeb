# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *
import sys
import json
#fb
internUrl='https://www.facebook.com/careers/university/internships/engineering'
gradUrl='https://www.facebook.com/careers/university/grads/engineering'

def createJson(url,keyword):
	html = urllib.urlopen(url).read()
	soup = BeautifulSoup(html)
	b = soup('a')
	jobs=[]
	uid=0
	for tag in b:
		if tag is not None and len(tag)>0:
			if keyword in (str(tag.contents[0])).lower():
				txt={}
				txt['id']=uid
				txt['title']=(tag.contents[0])
				txt['url']='https://www.facebook.com'+tag.get('href')
				uid+=1
				jobs.append(txt)
	return jobs

internships=createJson(internUrl,'intern')
newgrad=createJson(gradUrl,'grad')
print json.dumps({'facebook':{'intern':internships,'grad':newgrad}}, ensure_ascii=True)
#txt=json.loads(result)
#	f.write(str(txt))
# print myspan[0].contents

 