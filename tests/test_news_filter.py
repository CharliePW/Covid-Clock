from tests.new_news_filter import get_news

def test_get_news_status():
    x = get_news()
    assert(x["status"] == 'ok')

def test_get_news_articles():
    x = get_news()
    articles = x["articles"]
    assert(len(articles) > 0)
