from django.shortcuts import render ,get_object_or_404
from .models import Post ,User
from django.views.generic import (ListView,DetailView,
                                  CreateView,UpdateView,DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.core.mail import send_mail,BadHeaderError
from .forms import ContactForm
from django.http import HttpResponse
from django.contrib import messages



'''def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)'''

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3

class PostDetailView(DetailView):
    model = Post

'''class UserProfileView(DetailView):
    model = User
    template_name = 'blog/user_profile.html'

    def get_context_data(self , **kwargs):
        context  = super().get_context_data(**kwargs)
        context['user_id']= User.objects.get(id=context)
        return context
'''

def get_user_profile(request,username):
    user = User.objects.get(username=username)
    return render(request,'blog/user_profile.html',{'user':user })

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    context = {
        'posts': Post.objects.all().order_by('-date_posted')
    }

    return render(request, 'blog/about.html', context)

def contact_us (request):
    if request.method =='GET':
        form = ContactForm()
    else:
        form= ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject,message,from_email,['amdavy12@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            messages.success(request, 'Your  message has been sent !')
            return render(request, 'blog/contact_us_success.html', {'title': 'contact_us_success'})


    return render(request , 'blog/contact_us.html', {'form':form})

def contact_us_success(request):
    return render(request,'blog/contact_us_success.html',{'title':'contact_us_success'})
