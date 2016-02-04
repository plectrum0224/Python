import urllib2
import urlparse
import re

from bs4 import BeautifulSoup

response = urllib2.urlopen("http://baike.baidu.com/view/21087.htm")
if response.getcode() == 200:
    content = response.read()
    new_urls = set()
    soup = BeautifulSoup(content, 'html.parser', from_encoding = 'utf-8')
    links = soup.find_all('a', href = re.compile(r"/view/\d+\.htm"))
    for link in links:
        new_url = link['href']
        new_urls.add(new_url)
    for url in new_urls:
        print url