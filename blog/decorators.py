from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from blog.models import Article


def author_only(view_func):
    """
    decorator which check article was written by user or not.
    If was written then run view function...
    view function must have article_id as argument.
    :param view_func:
    :return view_func or HttpResponse with status 403:
    """
    def wrapper(request, article_id, *args, **kwargs):
        author_id = get_object_or_404(Article, id=article_id).author.id
        if request.user.id == author_id:
            print(1)
            return view_func(request, article_id, *args, **kwargs)
        else:
            return HttpResponse(status=403)
    return wrapper
