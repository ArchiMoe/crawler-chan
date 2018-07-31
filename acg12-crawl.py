import requests
import bs4
from time import strftime
user_agent = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
p=requests.get('https://acg12.com/category/pixiv/',headers=user_agent)
page=p.content
print('GO!')
bs_obj = bs4.BeautifulSoup(page,'lxml')
a_list = bs_obj.findAll('a',attrs={'href':True,'class':'inn'
                                                       '-archive__item__thumbnail__container '
                                                       'inn-card_painting__item__thumbnail'
                                                       '__container inn-card__thumbnail__container '
                                                       'inn-card__thumbnail__container_painting'})
addrlist=[]
c=0
for href in a_list:
    addrlist.append(href['href'])
print(addrlist)
c=0
srl=[]
for addr in addrlist:
    pg = requests.get(addr, headers=user_agent)
    pgb=pg.content
    pgb_o=bs4.BeautifulSoup(pgb,'lxml')
    imgurl=pgb_o.find_all('a',attrs={'href':True,'rel':'noopener'})
    for sr in imgurl:
        if sr.string==None:
            # print(sr['href'])
            c+=1
            fn = sr['href']
            pf = requests.get(fn, headers=user_agent)
            pfb = pf.content
            o = open('pic/%s.jpg' % c, 'wb')
            o.write(pfb)
            o.close()
            print('\r图片%s' % c + '已下载', end='')


        else:
            continue
print('完毕！')