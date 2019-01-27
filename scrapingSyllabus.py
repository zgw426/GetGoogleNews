import requests,bs4,re

get_url_info = requests.get('https://news.google.com/?hl=ja&gl=JP&ceid=JP%3Aja')
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
