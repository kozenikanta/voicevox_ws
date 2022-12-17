#import moduel
from requests_html import HTMLSession

#Instance
session = HTMLSession()

#get URL
url = 'https://news.google.com/home?hl=ja&gl=JP&ceid=JP:ja'
r = session.get(url)

#HTML => TXT
r = r.text

#out put
print(r)
