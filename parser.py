#-*- coding: utf-8 -*-

#import mpdule
import re
from urllib import request
from requests_html import HTMLSession

#Instance
session = HTMLSession()

#class
class Parser():
    def __init__(self):
        
        #decid tag
        self.dic = {'o':'おすすめ', 'f':'フォロー中', 'j':'日本', 'w':'世界', 'l':'ローカル', 'b':'ビジネス'}
        
   #select tag
    def showcase(self, p, v):
        print(self.dic[v])
        word =r'class="brSCsc"(.*?)'+self.dic[v]+'</a>'
        result = re.search(word,p)
        print(result)
        result=result.group()
        print(result)
        return result

    #extract where the title is written
    def div_parser(self,p):
        result = re.findall(r'class="WwrzSb(.*?)</a>',p)
        print(result)
        return result

    #extract the title
    def aria_label(self, p):
        result = re.findall('aria-label="(.*?)"',p)
        result = ''.join(result)
        print(result)
        return result

    #extract URL
    def URL_articles(self,txt,url):
        result = re.findall(r'href="./(.*?)"', txt)
        result = ''.join(result)
        result = url + result
        print(result)
        return result


if __name__ == "__main__":
    #Instance
    parser = Parser()
    
    #URL
    url = 'https://news.google.com/'
    
    #your country's setting(Japan)
    params = {'hl':'ja', 'gl':'JP', 'ceid':'JP:ja'}

    #loading URL
    r = session.get(url,params=params)

    #HTML => STR
    r = r.text
    
    #extract where the title is written
    a = parser.div_parser(r)

    #extract the title
    for i in a:
        c = parser.aria_label(i)

    #select tag
    b = parser.showcase(r, 'o')
    
