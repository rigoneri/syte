import re
import os
from os import listdir


def list_articles(articles_dir, extensions):
    """
    Build a dictionary of articles from the articles directory, separated by 
    category.
    """

    articles = dict()
    for file_ in listdir(articles_dir):
        if file_.endswith(extensions):
            with open(os.path.join(articles_dir, file_), 'r') as f:
                lines = f.read().split('\n')
                
                title = lines.pop(0).strip()
                category = lines.pop(0).strip()
                slug = slugify(title)
                source = '\n'.join(lines)
            
                if category in articles:
                    article_info = dict(title=title, slug=slug, source=source)
                    articles[category].append(article_info)
                else:
                    article_info = dict(title=title, slug=slug, source=source)
                    articles[category] = [article_info]
    return articles


def slugify(text):
    """
    Generates an ASCII-only slug.
    """
    return re.sub('-$', '', re.sub('[^A-Za-z0-9\-]+', '-', text))
