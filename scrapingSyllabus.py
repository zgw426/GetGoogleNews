#--------------------#
#C:>python GetGoogleNews.py
#Traceback (most recent call last):
#  File "GetGoogleNews.py", line 1, in <module>
#    import requests,bs4,re
#ModuleNotFoundError: No module named 'requests'
#
#$ pip install requests
#--------------------#
#C:\Users\crt02621\Data\python>python GetGoogleNews.py
#Traceback (most recent call last):
#  File "GetGoogleNews.py", line 1, in <module>
#    import requests,bs4,re
#ModuleNotFoundError: No module named 'requests'
#
#$ pip install beautifulsoup4
#--------------------#
#C:>python GetGoogleNews.py
#Traceback (most recent call last):
#  File "GetGoogleNews.py", line 22, in <module>
#    bs4Obj = bs4.BeautifulSoup(get_url_info.text, 'lxml')
#  File "C:\Users\crt02621\AppData\Local\Programs\Python\Python37\lib\site-packages\bs4\__init__.py", line 196, in __init__
#    % ",".join(features))
#bs4.FeatureNotFound: Couldn't find a tree builder with the features you requested: lxml. Do you need to install a parser library?
#
#$ pip install lxml

import requests,bs4,re

### rev.01
def getInfoFromGoogleNews(argUrl):
    get_url_info = requests.get( argUrl )
    bs4Obj = bs4.BeautifulSoup(get_url_info.text, 'lxml')
    tmplist = bs4Obj.select('div h4')
    newslist = [[]]
    for item in tmplist:
        patn = 'href="(.*)".*<span>(.*)</span>'
        tmpinfo = re.search(patn , str( item ) )
        newslist.append([tmpinfo.group(2),tmpinfo.group(1)])
    for news in newslist:
        for obj in news:
            print(obj)
        print("********************************************************************")

# http://www.google.co.jp/search?q=aws+site:https://aws.amazon.com/jp/blogs/news/&tbs=qdr:d
# http://www.google.co.jp/search?hl=jp&gl=JP&num=10&q=aws&tbs=qdr:d
        
#url = 'https://news.google.com/?hl=ja&gl=JP&ceid=JP%3Aja'
#getInfoFromGoogleNews( url )


### rev.02

def getInfoFromGoogleSearch(argUrl):
    get_url_info = requests.get( argUrl )
    bs4Obj = bs4.BeautifulSoup(get_url_info.text, 'lxml')
    #print(bs4Obj)
    tmplist = bs4Obj.select('a')
    #print(tmplist)
    newslist = [[]]
    listNo = 1

    for item in tmplist:
        print( listNo, " : ", item )
        outTitle=""
        outUrl=""
        patn = 'href="/url?q=(http.*)".*>(.*)</a>'
        tmpinfo = re.search(patn , str( item ) )
        try:
            outTitle = tmpinfo.group(1)
            outUrl   = tmpinfo.group(2)
        except:
            outTitle = listNo
            outUrl   = "url"
            listNo += 1
        #newslist.append([tmpinfo.group(2),tmpinfo.group(1)])
        newslist.append([outUrl,outTitle])
    for news in newslist:
        for obj in news:
            print(obj)
        print("ーーー")


url='http://www.google.co.jp/search?hl=ja&source=hp&q=aws&tbs=qdr:d'
getInfoFromGoogleSearch( url )
