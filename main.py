import parser, voicevox
from time import sleep
from playsound import playsound
from requests_html import HTMLSession 

#Instance
parser = parser.Parser()
voice = voicevox.voicevox()
session = HTMLSession()

#URL
url = 'https://news.google.com/'
    
#your country's setting(Japan)
params = {'hl':'ja', 'gl':'JP', 'ceid':'JP:ja'}

#loading URL
r = session.get(url,params=params)

#HTML => STR
r = r.text
    
#extract where title is written
print('class')
a = parser.div_parser(r)
print('')

b = []

#extract title
print('title')
for i in a:
    c = parser.aria_label(i)
    b.append(c)
print(b)


for i in b:
    voice.voicevox(i)
    playsound('news.wav')

