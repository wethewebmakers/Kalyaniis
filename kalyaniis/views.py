import re
from django.shortcuts import render, redirect
from .models import *
from django.http import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
import json
from django.contrib import messages

def auth_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/updateproducts')
            else:
                return redirect('/login')
        else:
            message = 'Invalid Credentials! Please try again!!'
            return render(request, 'login.html', {'message': message})
    else:
        return render(request, 'login.html')

def auth_logout(request):
    logout(request)
    return redirect('/home')

def updateform(request):
    if request.user.is_authenticated:
        return render(request, 'updateform.html')
    else:
        return redirect('/home')

def home(request):

    silksarees = Products.objects.all().filter(category='silksarees').order_by('date_uploaded').reverse()[:3]
    designersarees = Products.objects.all().filter(category='designersarees').order_by('date_uploaded').reverse()[:3] 
    kurtis = Products.objects.all().filter(category='kurtis').order_by('date_uploaded').reverse()[:3]
    lehengas = Products.objects.all().filter(category='lehenga').order_by('date_uploaded').reverse()[:3]
    
    return render(request, 'home.html', {'silksarees': silksarees, 'designersarees': designersarees, 'kurtis': kurtis, 'lehengas': lehengas})


def productcategory(request, category):
    products_list = Products.objects.all().filter(category=category).order_by('date_uploaded').reverse()
    # products_list = Products.objects.all().filter(category=category).order_by('?')

    paginator = Paginator(products_list, 24)
    page = request.GET.get('page', 1)
    productss = paginator.get_page(page)
    
    return render(request, 'productgrid.html', {'productss': productss, 'category': category})


def productdetail(request, pid):
    product = Products.objects.get(product_id = pid)
    params = [product.image1, product.image2, product.image3, product.image4, product.image5]
    images = []
    print(product.image1, product.image2, product.image3, product.image4, product.image5, product.video)
    for item in params:
        if item:
            img = list(str(item).split('/'))
            print(item, img)
            if len(img)>2 and img[-1]!='' :
                images.append(item)

    video = 0
    if product.video:
        vid = list(str(product.video).split('/'))
        if len(vid)>2 and vid[-1]!='':
            video=1
    else:
        video=0
    return render(request, 'productdetail.html', {'product': product, 'images': images, 'video': video})

def addproduct(request):
    productname = request.POST.get('productname').title()
    category = request.POST.get('category')
    description = request.POST.get('description')
    image1 = request.POST.get('image1').split('\\')[-1]
    image2 = request.POST.get('image2').split('\\')[-1]
    image3 = request.POST.get('image3').split('\\')[-1]
    image4 = request.POST.get('image4').split('\\')[-1]
    image5 = request.POST.get('image5').split('\\')[-1]
    video = request.POST.get('video').split('\\')[-1]
    
    Products.objects.create(productname = productname, category = category, description = description, image1 = 'static/images_uploaded/'+image1, 
                            image2 = 'static/images_uploaded/'+image2, image3 = 'static/images_uploaded/'+image3, image4 = 'static/images_uploaded/'+image4, image5 = 'static/images_uploaded/'+image5, video = 'static/images_uploaded/'+video)
    
    return JsonResponse({'message': 'Product added successfully !!'})

def deleteproduct(request):
    pid = request.POST.get('product_id')
    
    response = Products.objects.get(product_id = pid).delete()
    return JsonResponse({'message': 'Deleted successfully'})


    