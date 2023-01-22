#import moduel
from requests_html import HTMLSession
import re

class sample():
    
    def request_html(self):
        #Instance
        session = HTMLSession()
        #get URL
        url = 'https://news.google.com/home?hl=ja&gl=JP&ceid=JP:ja'
        r = session.get(url)
        #HTML => TXT
        r = r.text
        #out put
        print(r)


    def regex(self):
        text = r'I have a pen'
        print('######### findall ##########')
        print(re.findall('a' , text))

        print('######### search ##########')
        print(re.search('I',text))
        print(re.search('ave',text))

        print('######### match ##########')
        print(re.match('I', text))
        print(re.match('ave',text))

if __name__ == "__main__":
    a = sample()
    b = input('choise sanple(scraping, regex)')
    print(b)
    if b == 'scraping':
        a.request_html()
    elif b == 'regex':
        a.regex()
