from django.shortcuts import render, get_object_or_404, reverse, HttpResponseRedirect
from . import WikiAPI
from .models import Article
from .forms import ArticleEditForm, ArticleSearchForm


def index(request):
    if request.method == 'POST':
        form = ArticleSearchForm(request.POST)
        if form.is_valid():
            article_title = form.cleaned_data.get('search_title')
            return HttpResponseRedirect(reverse(get_article, args=[article_title]))
    else:
        form = ArticleSearchForm()
    return render(request, 'mainapp/index.html', {'form': form})


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
    if request.method == 'POST':
        form = ArticleEditForm(request.POST)
        if form.is_valid():
            new_html = form.cleaned_data.get('new_markup')
            new_last_edited_by = form.cleaned_data.get('pseudonym')
            wiki_article.article_html = new_html
            wiki_article.last_edited_by = new_last_edited_by
            wiki_article.save()
            return HttpResponseRedirect(reverse(get_article, args=[title]))
    else:
        form = ArticleEditForm(initial={'new_markup': wiki_article.article_html})
    return render(request, 'mainapp/article_edit.html', {'article': wiki_article, 'form': form})
