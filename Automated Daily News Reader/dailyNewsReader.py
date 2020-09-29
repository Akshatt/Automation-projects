from newsapi import NewsApiClient
from win32com.client import Dispatch


class News:
    def __init__(self):
        self.akey = '6844359fe5fc47dcb5c240106eefa2b0'
        self.get_news()

    def speak(self, strng):
        speak = Dispatch("SAPI.SpVoice")
        speak.Speak(strng)

    def get_news(self):
        newsapi = NewsApiClient(api_key=self.akey)
        top_headlines = newsapi.get_top_headlines(category='general',
                                                  language='en',
                                                  country='in')
        for i, article in enumerate(top_headlines['articles']):
            if i == 5:
                break

            self.speak("Author : " + article['source']['name'])
            self.speak("Title : " + article['title'])
            self.speak("Content : " + article['content'])


if __name__ == '__main__':
    News()