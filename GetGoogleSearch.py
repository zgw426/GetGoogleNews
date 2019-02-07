# https://tanuhack.com/python/google-scraping/

#C:>python GetGoogleSearch.py
#Traceback (most recent call last):
#  File "C:\Users\crt02621\AppData\Local\Programs\Python\Python37\lib\site-packages\lxml\cssselect.py", line 13, in <module>
#    import cssselect as external_cssselect
#ModuleNotFoundError: No module named 'cssselect'
#
#During handling of the above exception, another exception occurred:
#
#Traceback (most recent call last):
#  File "GetGoogleSearch.py", line 18, in <module>
#    for a in root.cssselect('div#search h3.r a'):
#  File "C:\Users\crt02621\AppData\Local\Programs\Python\Python37\lib\site-packages\lxml\html\__init__.py", line 431, in cssselect
#    from lxml.cssselect import CSSSelector
#  File "C:\Users\crt02621\AppData\Local\Programs\Python\Python37\lib\site-packages\lxml\cssselect.py", line 16, in <module>
#    'cssselect does not seem to be installed. '
#ImportError: cssselect does not seem to be installed. See http://packages.python.org/cssselect/
# |
# pip install cssselect

import re
import json
import requests as rq
import lxml.html as lx

urlList01=[]
qryList = []
#qryList.append("実証&tbs=qdr:d")
qryList.append("IoT AWS&tbs=qdr:d")
qryList.append("AR&tbs=qdr:d")
qryList.append("JavaScript&tbs=qdr:d")

for search_query in qryList:
    r = rq.get('http://www.google.co.jp/search?hl=jp&gl=JP&num=5&q='+search_query)
    html = r.text.encode()		#コンテンツをエンコードする
    root = lx.fromstring(html)	#パース（lxmlでスクレイピングする準備をする）
    for a in root.cssselect('div#search h3.r a'):
        urlList01.append( re.sub(r'/url\?q=|&sa.*', '',a.get('href')) )

urlList02=[]
for url in urlList01:
    try:
        #print("ーーーーーーーーーーーーーーーーーー")
        #print(url)
        search = rq.get( url )
        search_html = search.text.encode(search.encoding)
        if(search.encoding=='utf-8' or search.encoding=='UTF-8'):
            search_root = lx.fromstring(search_html.decode('utf-8'))
        else:
            search_root = lx.fromstring(search_html)        
        list_title = []
        for a in search_root.cssselect('title'):
            list_title.append(a.text)     
        title=''
        for index,item in enumerate(list_title):
            if index==0:
                title = item
            else:
                title = title + ', ' +item
        #print("title: ", title)
        list_description = []
        for a in search_root.cssselect('meta[name="description"]'):
            list_description.append(a.get('content'))     
        description=''
        for index,item in enumerate(list_description):
            if index==0:
                description = item
            else:
                description = description + ', ' +item
        #print("description: ", description)
        list_keywords = []
        for a in search_root.cssselect('meta[name="keywords"]'):
            list_keywords.append(a.get('content'))     
        keywords=''
        for index,item in enumerate(list_keywords):
            if index==0:
                keywords = item
            else:
                keywords = keywords + ', ' +item
        #print("keywords: ", keywords)
        urlList02.append( [url, title, description, keywords] )
    except:
            print('読み取り不可')

urlList03 = []
for tgt in urlList02:
    print(tgt)
