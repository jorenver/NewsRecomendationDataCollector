from NewsCollectorService import NewsCollectorService
from model import Connect
from model import Article as ar

def main():
    service = NewsCollectorService()
    Connect.connect_to_db()
    print('Getting articles....')
    articles = service.get_articles('bitcoin', 'bbc-news,the-verge')
    print(f'Articles count: {len(articles)}')
    for a in articles:
        print(a)
        na = ar.Article(
            author=a['author'],
            title=a['title'],
            description=a['description'],
            url=a['url'],
            urlToImage=a['urlToImage'],
            content=a['content']
        )
        na.save()
        print(f"{na.id} -> {na.url}")
    print('Getting articles Done')


if __name__ == "__main__":
    main()