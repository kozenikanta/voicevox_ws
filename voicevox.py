#import module
from requests_html import HTMLSession
import json
from time import sleep
from playsound import playsound

session = HTMLSession()
class voicevox():
    def __init__(self):
        self.hostname = 'localhost'

    def voicevox(self,text):
        res1 = session.post('http://' + self.hostname + ':50021/audio_query',
                    params={'text': text, 'speaker': 1})
        res2 = session.post('http://' + self.hostname + ':50021/synthesis',
                    params={'speaker': 1},
                    data=json.dumps(res1.json()))
        with open('./news.wav', mode = 'wb') as f:
            f.write(res2.content)

if __name__ == "__main__":
    a = voicevox()
    b = ['アイス','しめ鯖']
    print(b)
    for i in b:
        a.voicevox(i)
        playsound('news.wav')
        
        
