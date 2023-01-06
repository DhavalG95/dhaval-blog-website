from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import login , authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request,'index.html')

def create(request):
    form_info = Info(request.POST or None )
    if request.method == "POST":
        if form_info.is_valid():
            form_info.save()
        else:
            print(form_info.errors)
        return redirect(blog)


    return render(request,'create.html',context={'form':form_info})


def myblog(request):
    
    if request.method == "POST":
        srch = request.POST.get('search')
        blog_info = Form.objects.filter(Q(Description__icontains=srch) | Q(Title__icontains=srch)).values()
        return render(request,'myblogs.html',context={'data':blog_info})

    blog_info = Form.objects.filter(Author=request.user.username).values()
    # print(blog_info)
    return render(request,'myblogs.html',context={'data':blog_info})

def blog(request):
        
    if request.method == "POST":
        srch = request.POST.get('search')
        blog_info = Form.objects.filter(Q(Description__icontains=srch) | Q(Title__icontains=srch)).values()
        return render(request,'blogs.html',context={'data':blog_info})
     
    blog_info = Form.objects.all().values()
    comments = Comment.objects.all().values()
    # print(blog_info)
    return render(request,'blogs.html',context={'data':blog_info,'data2':comments})

def blogcomment(request):
    
    comment_form = CommentForm(request.POST or None)
    if request.method == "POST":
        if comment_form.is_valid():
            comment_form.save()
        else:
            print(comment_form.errors)
        return redirect(blog)
        # return render(request,'comments.html',context={'comment_data':comment_form})
    
    return render(request,'comments.html',context={'comment_data':comment_form})


def edit(request,pk):
    blog_info = Form.objects.get(id=pk)
    form_info = Info(request.POST or None,instance=blog_info )
    if request.method == "POST":
        if form_info.is_valid():
            form_info.save()
        else:
            print(form_info.errors)
        return redirect(blog)

    blog_info = Form.objects.all().values()
    return render(request,'edit.html',context={'form':form_info,'data':blog_info})

def delete(request,pk):
    delt = Form.objects.filter(is_delete="False").values()
    blog_info = delt.objects.get(id=pk)
    # blog_info = Form.objects.get(id=pk)
    blog_info.update(is_delete=True)
    # blog_info.delete()
    return redirect(blog) 

def contact(request):
    if request.method=="POST":
        nam = request.POST.get('name')
        num = request.POST.get('number')
        emal = request.POST.get('email')
        qry = request.POST.get('query')
        Contactform.objects.create(Name=nam,Number=num,Email=emal,Query=qry)
        
        messages.success(request, f"Thanks For Contacting Us! We Will Get In Touch With You Shortly.....")
        return redirect(contact)

        # messages.error(request, 'Invalid form submission.')

    
   
    return render(request,'contact.html')

def thanks(request):
    return render(request,'thanks.html')

def register(request):
    reg_info = UserRegistrationForm(request.POST)
    if request.method == "POST":
        if reg_info.is_valid():
            reg_info.save()
            return redirect('login')
        else:
            print(reg_info.errors)
    else:
        reg_info=UserRegistrationForm()
        return render(request,'register.html',context={'forum':reg_info})
    
    return render(request,'register.html',context={'forum':reg_info})


