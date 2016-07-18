from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from .models import Post, Comment
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm, CommentForm
from django.core.mail import send_mail


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


# def post_list(request):
#     object_list = Post.published.all()
#     paginator = Paginator(object_list, 1)  # posts in each page
#     page = request.GET.get('page', 1)  # this indicate the current page number
#     try:
#         posts = paginator.page(page)  # obtain the object for the desired page by calling page() method
#     except PageNotAnInteger:
#         # if page is not an integer deliver the first page
#         posts = paginator.page(1)
#         # if the page is out of range deliver the last page of results
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
#     return render(request, 'blog/post/list.html', {'posts': posts})


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
    comments = post.comments.filter(active=True)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            # create comment object but don't save to database
            new_comment = comment_form.save(commit=False)
            # assign the current post to the comment
            new_comment.post = post
            # save the comment to the database
            new_comment.save()
            # return redirect('post_detail')
    else:
        comment_form = CommentForm()
    return render(request, 'blog/post/detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # form.cleaned_data is always invoked after .is_valid(), otherwise will raise AttributeError
            cd = form.cleaned_data
            # then do something with data in cd
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = '{}({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at {}\n\n{}\s comments: {}'.format(post.title, post_url, cd['name'], cd['comments'])
            send_mail(subject, message, 'testeur.three@gmail.com', [cd['to']])
            sent = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post, 'form': form, 'sent': sent})
