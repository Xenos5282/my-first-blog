from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import get_object_or_404
from .models import Post
>>>>>>> d9a24b2545eb7d75e7ce17b5a411c5897671f41e

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
