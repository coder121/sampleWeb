# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib
from BeautifulSoup import *
import sys
import json

#url = raw_input('Enter - ')
f = open('jobs2.json', 'w')
url='https://jobs.cisco.com/go/New-Graduate-Internships-Engineering-Jobs/531400/'
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
# Retrieve all of the anchor tags
a=soup('a')
# Look at the parts of a tag
'''
    print 'TAG:',tag
    print 'URL:',tag.get('href', None)
    print 'Contents:',tag.contents[0]
    print 'Attrs:',tag.attrs'''
#for tag in tags:
jobs=[]
uid=0
def createJson():	
	global uid
	tags = soup('tr')
	for t in tags:
		link=t.find('a',{'class':'jobTitle-link'})
		# myspan.append(t.findAll('span'))
		if link:
			txt={}
			#txt='{title:'+link.text+',url:'+'jobs.cisco.com'+link.get('href')+'}'
			txt['id']=uid
			txt['title']=link.text
			txt['url']='jobs.cisco.com'+link.get('href')
			jobs.append(txt)
			uid+=1



createJson()		
for tag in a:
	if tag.get('class')=="paginationItemFirst":
		html = urllib.urlopen("https://jobs.cisco.com"+tag.get('href')).read()
		soup = BeautifulSoup(html)
		createJson()
		break

result=json.dumps({'cisco':jobs}, ensure_ascii=True)
f.write(unicode(result))
#txt=json.loads(result)
#	f.write(str(txt))
# print myspan[0].contents

 