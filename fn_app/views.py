from django.shortcuts import render,redirect
from fn_app.models import post
from fn_app.forms import Article_Form,TitleForm
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.

def Home(request):
    context={
         'post':post.objects.all().order_by('-date_posted'),#displaying the data from the database

    }

    return render(request, 'templates/article/home.html', context) #to create the webpage




def Validate(request):# to check admin has posted some title or not
    if request.method=='POST':
        form = TitleForm(request.POST)# getting title from html page
        if form.is_valid():
            article = post(
                title=request.POST.get('title', '')#storing title
            )
            article.save()#save method is used to store the data permantly into database
            return redirect('home')#taking back to the hoempage
        else:
            return redirect('logout')
    else:
        form = TitleForm()
        return render(request,'templates/article/admin.html',{'form':form})#creating the html page and displaying our form



def ArticleView(request):
    if request.method=='POST':
        form = Article_Form(request.POST)#storing the form data
        if form.is_valid():
            title = request.POST.get('title')
            content = request.POST.get('content')
            author = request.POST.get('author')

            db = post(
                title = title,
                content = content, #used for storing the values in database
                author = author,
            )
            check = post.objects.filter(title=title)# to check whter admin have passed the title or not
            if check.exists():#if passed save the data into the database
                db.save()

                return render(request,'templates/article/geniune.html')
            else:

                return render(request,'templates/article/fake.html')

    else:
        aform = Article_Form()
        return render(request,'templates/article/post.html',{'form':aform})
