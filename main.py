
import requests
from lxml import etree


txt = '221.232.105.110:8880'
url = f'http://tonkiang.us/alllist.php?s={txt}&c=false'

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Connection':'keep-alive',
    'DNT': '1',
    'Host': 'tonkiang.us',
    'Referer': f'http://tonkiang.us/hotellist.html?s={txt}',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

r = requests.get(url,headers=headers)
# print(r.content.decode())

div_list = etree.HTML(r.content.decode()).xpath('//div[@class="tables"]/div')

with open('iptv.m3u', 'w', encoding='utf8') as f:
    f.write('#EXTM3U\n')
    for div in div_list:
        title = div.xpath('./div[@class="channel"]//div[@style="float: left;"]/text()')
        title = title[0] if title else None
        # url = div.xpath('./div[@class="m3u8"]//td[@style="padding-left: 6px;"]/text()')
        url = div.xpath('./div[@class="m3u8"]//td[starts-with(@style,"padding")]/text()')
        url = url[0].strip() if url else None
        if title and url:
            f.write(f'#EXTINF:-1,{title}\n{url}\n')



