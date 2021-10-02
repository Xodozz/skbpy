from django.views import generic
from django.http import HttpResponse,HttpResponseNotFound
from .models import Post

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3
class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
class HomePage(generic.ListView):
    model = Post
    template_name = 'home.html'
def index(request):
    return HttpResponse('Страница')

