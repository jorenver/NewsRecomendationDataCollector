from newsapi import NewsApiClient

class NewsCollectorService:
    def __init__(self):
        self.newsapi = NewsApiClient(api_key='0b78a1df1e264b8cb9d46128246174fc')

    def get_sources(self):
        sources = self.newsapi.get_sources()
        return sources['sources']

    def get_articles(self, topic, source):
        response = self.newsapi.get_everything(q=topic,
                          sources=source,
                          language='en',
                          sort_by='relevancy',
                          page=1)
        return response['articles']
