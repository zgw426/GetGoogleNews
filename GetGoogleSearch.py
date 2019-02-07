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
from janome.tokenizer import Tokenizer

urlList01=[]
qryList = []
#qryList.append("実証&tbs=qdr:d")
qryList.append("IoT AWS&tbs=qdr:d")
#qryList.append("AR&tbs=qdr:d")
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
        addFlg = 1
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

        pattern = '(?!(Page Not Found|Too Many Requests|Error report))'
        result = re.match(pattern, title)
        if result:
            print("1 : ", result)
            addFlg = 1
        else:
            print("2 : ", result)
            addFlg = 0
        #print("result = ", result)
        """
        if title == "Page Not Found":
            addFlg = 0
        if title == "Too Many Requests":
            addFlg = 0
        """
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
        if addFlg == 1:
            urlList02.append( [url, title, description, keywords] )
    except:
            print('読み取り不可')

urlList03 = []

#"""
for tgt in urlList02:
    print("^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("title", tgt[1] , "\n", "description", tgt[2], "\n", tgt[3], "\n", tgt[0])
    print("____________________________")
#"""
"""
for tgt in urlList02:
    col = 0
    data = []
    each_data = []
    t = Tokenizer()
    tmpStr = tgt[1]+" "+tgt[2]+" "+tgt[3]
    tokens = t.tokenize( tmpStr )
    for token in tokens:
        partOfSpeech = token.part_of_speech.split(',')[0]
        each_data.append(token.surface)
    data.append(each_data)
    each_data = []
    datastr = map(str, data[0])
    s1 = " "
    wStr = s1.join(datastr)
    print( wStr )
"""
