from django.shortcuts import render,redirect

from django.views.generic import CreateView,ListView,DetailView,UpdateView

from vfapp.models import MyUser,Comments

from vfapp.forms import RegistrationForm,EditProfileForm

from django.utils.decorators import method_decorator


#create your view here.

from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic import FormView
from vfapp.forms import LoginForm,PostForm
from django.contrib.auth import authenticate,login,logout
from vfapp.models import Posts

def signin_reqired(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)
    return wrapper

@method_decorator(signin_reqired,name='dispatch')
class ProfileView(CreateView):
    template_name="addpost.html"
    form_class=PostForm
    model=Posts
    success_url=reverse_lazy("index")
    context_object_name="posts"

    def form_valid(self, form):

        form.instance.user=self.request.user

        return super().form_valid(form)



@method_decorator(signin_reqired,name='dispatch')
class IndexView(ListView):
    template_name='home.html'
    form_class=PostForm
    model=Posts
    success_url=reverse_lazy("index")
    context_object_name="posts"
    

    
    def get_queryset(self):
        return Posts.objects.all()

#                                                    registration view!!!!!!


class SignupView(CreateView):

    model=MyUser

    form_class=RegistrationForm

    template_name='register.html'
    success_url=reverse_lazy('signin')

                                                      # creating login view!!!

class LoginView(FormView):

    form_class=LoginForm

    template_name='login.html'

    def post(self,request,*args,**kw):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get('password')
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect('index')

            else:

                return render(request,self.template_name,{'form':form})


@method_decorator(signin_reqired,name='dispatch')
class PostDetailView(DetailView):
    model=Posts
    template_name: str="post-detail.html"
    pk_url_kwarg="id"
    context_object_name="posts"

@signin_reqired
def add_comment(request,*args,**kw):
    qid=kw.get("id")
    post=Posts.objects.get(id=qid)  
    comment=request.POST.get("comment")
    Comments.objects.create(User=request.user,comment=comment,post=post)
    return redirect("index")

@signin_reqired
def like_view(request,*args,**kwargs):
    id=kwargs.get('id')
    pst=Posts.objects.get(id=id)
    pst.like.add(request.user)
    pst.save()
    return redirect('index')


@signin_reqired
def signout_view(request,*args,**kwargs):
    logout(request)
    return redirect("signin")

@method_decorator(signin_reqired,name='dispatch')
class ImageView(ListView):
    model=Posts
    template_name='profile.html'
    context_object_name='images'

    def get_queryset(self):
        return Posts.objects.filter(user=self.request.user)

@method_decorator(signin_reqired,name='dispatch')
class EditprofileView(UpdateView):
    model=Posts
    template_name="profile-edit.html"
    form_class=EditProfileForm
    pk_url_kwarg="id"
    success_url=reverse_lazy('index')

def remove_post(request,*args,**kwargs):
    id=kwargs.get('id')
    Posts.objects.get(id=id).delete()
    return redirect('index')