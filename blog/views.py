from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.decorators.http import require_http_methods

from blog.decorators import author_only
from blog.forms import ArticleForm
from blog.models import Article


@require_http_methods(['GET'])
def show_articles(request):
    """
    method for getting page with articles
    :param request:
    :return TemplateResponse:

    param request can has tuple with GET parameters:
    :parameter page: show page number; default = 1
    :parameter page_length: show how much articles will be on page; default = 12
    """
    args = {}
    page = 1
    page_length = 12
    if request.GET.get('page'):
        page = int(request.GET.get('page'))
    if request.GET.get('page_length'):
        page_length = int(request.GET.get('page_length'))
    article_query = Article.objects.all().order_by('publication_date').reverse()
    paginator = Paginator(article_query, page_length)
    articles = paginator.page(page)
    paginator.page_lrange = range(1, paginator.num_pages + 1)
    paginator.current_page = page
    args['articles'] = articles
    args['paginator'] = paginator
    return render(request, 'articles.html', args)


def get_article(request, article_id):
    args = {}
    article = get_object_or_404(Article, id=article_id)
    args['article'] = article
    return render(request, 'article.html', args)


@login_required
def create_article(request):
    args = {}
    form = ArticleForm()
    if request.POST:
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            messages.add_message(request, messages.INFO, 'Статья опубликована')
            return redirect('index')
    args['form'] = form
    return render(request, 'cr_up_article_page.html', args)


@login_required
@author_only
def update_article(request, article_id):
    args = {}
    article = get_object_or_404(Article, id=article_id)
    form = ArticleForm(instance=article)
    if request.POST:
        form = ArticleForm(data=request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.INFO, 'Успешно изменено')
            return redirect('index')
    args['form'] = form
    return render(request, 'cr_up_article_page.html', args)


@login_required
@author_only
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    messages.add_message(request, messages.INFO, 'Успешно удалёно')
    return redirect('index')
