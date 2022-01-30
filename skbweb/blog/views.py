from django.views import generic
from django.http import HttpResponse,HttpResponseNotFound
from .models import Post,Banner
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.db.models import Q
from django.template import RequestContext


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3

    def index_page(request):
        posts = Post.objects.all().order_by('-id')

        if 'page' in request.GET:
            page = request.GET['page']
        else:
            page = 1
        paginator = Paginator(posts, 15)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        context = {
            'posts': posts
        }
        # return render(request, "pages/index.html", context)
        return render(request, "index.html", context)
class PostDetail(generic.DetailView):

    model = Post
    template_name = 'post_detail.html'
class HomePage(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'home.html'
    paginate_by = 3
    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['settings'] = Banner.objects.all().order_by('-id')
        return context
# class BannerList(generic.ListView):
#     model = Banner
#     template_name = 'banner.html'
#
#     banner_list = Banner.objects.all().order_by('-id')
#     context = {"banner_list": banner_list}

class BannerGet(generic.ListView):
    model = Banner
    template_name = 'home.html'


def index(request):
    return HttpResponse('Страница')

class SearchResultsView(ListView):
    model = Post

    template_name = 'search_results.html'

    def get_queryset(self):

        query = self.request.GET.get('q')
        if query!='':

            object_list = Post.objects.filter(
                Q(title__icontains=query, status=1)
                )

        return object_list


def e_handler404(request,exception):
    response = render(request, 'error404.html', status=404)
    return response


def e_handler500(request):

    response = render(request,'error500.html',status=500)

    return response