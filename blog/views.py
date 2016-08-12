from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify


# Create your views here.\
class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


def blog_list(request):
    p = Post.objects.all().order_by('-published_date')
    print(p)
    context_dict = {'post': p}
    return render(request, 'blog_list.html', context_dict)

def home(request):
    return render(request, 'home.html', {})


def blog(request, slug, cat):
    post = Post.objects.get(slug=slug)
    context_dict = {'post': post}
    return render(request, 'post.html', context_dict)


def cat(request, cat):
    post = Post.objects.filter(category__slug=cat)
    context_dict = {'post': post}
    return render(request, 'category.html', context_dict)


class EditPost(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['category', 'title', 'slug', 'img', 'content']
    template_name = 'edit_post.html'
    success_url = '/'

class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['category', 'title', 'content', 'img']
    success_url = '/'
    template_name = 'post_new.html'

    def form_valid(self, form):
        user = self.request.user
        form.instance.author = user
        form.instance.slug = slugify(form.instance.title)
        return super(CreatePost, self).form_valid(form)

class DeletePost(DeleteView):
    model = Post
    success_url = '/blog/'
    template_name = 'confirm_delete.html'

def contact_page(request):
    return render(request, 'contact_page.html')

def about_me(request):
    return render(request, 'about.html')

# def portfolio(request):