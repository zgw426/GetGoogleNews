# https://tanuhack.com/python/google-scraping/

#C:\Users\crt02621\Data\python>python GetGoogleSearch.py
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
#import gspread
#from oauth2client.service_account import ServiceAccountCredentials 


search_query = "aws&tbs=qdr:d"

#requestsのget関数を使用して、Googleの検索結果画面(10位まで)の情報を抜き出す
r = rq.get('http://www.google.co.jp/search?hl=jp&gl=JP&num=10&q='+search_query)
html = r.text.encode()		#コンテンツをエンコードする
root = lx.fromstring(html)	#パース（lxmlでスクレイピングする準備をする）

for a in root.cssselect('div#search h3.r a'):
    print(  re.sub(r'/url\?q=|&sa.*', '',a.get('href'))  )
