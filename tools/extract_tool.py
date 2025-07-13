from newspaper import Article
def extract_text(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        return article.text
    except Exception as e:
        return f"Error extracting text from {url}: {str(e)}"
    
