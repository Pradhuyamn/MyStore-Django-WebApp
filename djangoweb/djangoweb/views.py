from django.http import HttpResponse
from django.shortcuts import render,redirect
from myapp.models import *

def show_about_page(request):
    name = 'Pradhuyamn Neema'
    email = 'pradhuyamn@nykinsky.com'
    data = {
        'name': name,
        'email': email
    }
    return render(request, "about.html", data)


def show_home_page(request):
    cats = Category.objects.all()
    images = Image.objects.all()
    data = {'images': images , 'cats': cats}
    return render(request, "home.html", data)


def show_category_page(request, cid):
    cats = Category.objects.all()
    categ = Category.objects.get(pk=cid)
    images = Image.objects.filter(cat=categ)
    data = {'images': images , 'cats': cats}
    return render(request, "home.html", data)


def home(request):
    return redirect('/home')

def search(request):
    query = request.GET['query']
    catsTitle = Category.objects.filter(title__icontains=query)
    catsDes = Category.objects.filter(description__icontains=query)
    cats = catsTitle.union(catsDes)
    imagesTitle = Image.objects.filter(title__icontains=query)
    imagesDes = Image.objects.filter(description__icontains=query)
    images = imagesTitle.union(imagesDes)
    data = {'images': images, 'cats': cats, 'query' : query }
    return render(request,'search.html',data)
