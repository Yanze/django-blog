from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_list(request):
    posts = Post.published.all()
    object_list = Post.published.all()
    paginator = Paginator(object_list, 3)  # posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post/list.html', {'page': page, 'posts': posts})


def post_detail(request, year, month, day, post):
    """
    get_object_or_404(klass, *args, **kwargs)
    - klass: it can be a Model class, a Manager, or a querySet instance from which to get the object
    - **kwargs: lookup parameters, which should be in the format accepted by get() and filter()
    - will return only one object

    EXAMPLLE:
        my_object = get_object_or_404(MyModel, pk=1)

        equals to:

        try:
        my_object = MyModel.objects.get(pk=1)
    except MyModel.DoesNotExist:
        raise Http404("No MyModel matches the given query.")
    """
    post = get_object_or_404(Post, slug=post)
    return render(request, 'blog/post/detail.html', {'post': post})
