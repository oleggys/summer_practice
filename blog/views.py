from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from django.views.decorators.http import require_http_methods
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
    article_query = Article.objects.all()
    paginator = Paginator(article_query, page_length)
    articles = paginator.page(page)
    paginator.page_lrange = range(1, paginator.num_pages + 1)
    paginator.current_page = page
    args['articles'] = articles
    args['paginator'] = paginator
    return render(request, 'articles.html', args)


def article_view(request, article_id):
    if request.method == 'POST':
        pass
    elif request.method == 'GET':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass


def get_article(request, article_id):
    args = {}
    article = Article.objects.get(id=article_id)
    args['article'] = article
    return render(request, 'article.html', args)

