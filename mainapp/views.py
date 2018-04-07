from django.shortcuts import render, get_object_or_404
from . import WikiAPI
from .models import Article


def index(request):
    return render(request, 'mainapp/index.html', {})


def get_article(request, title):
    wiki_articles = Article.objects.filter(title=title)
    if wiki_articles.exists():
        print('--FROM DATABASE--')
        wiki_article = get_object_or_404(Article, title=title)
    else:
        print('--DRAWING FROM WIKIPEDIA--')
        html = WikiAPI.get_article_HTML(title)
        wiki_article = Article(title=title, article_html=html)
        wiki_article.save()
    return render(request, 'mainapp/article.html', {'article': wiki_article})


def edit_article(request, title):
    wiki_article = get_object_or_404(Article, title=title)
    return render(request, 'mainapp/article_edit.html', {'article': wiki_article})
