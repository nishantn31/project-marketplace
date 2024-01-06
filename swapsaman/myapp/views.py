from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse,JsonResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from myapp.models import *
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    context ={}
    cats = Category.objects.all().order_by('name')
    context['categories'] = cats
    products = Product.objects.all().values()
    context['products'] = products
    images = ProductImage.objects.all()
    
    product_images_dict = {}
    for i in images:
        if i.product_id.pk not in product_images_dict:
            product_images_dict[i.product_id.pk] = []
        product_images_dict[i.product_id.pk].append(i.product_image)
    
    for product in products:
        product["image"] = product_images_dict[product["id"]][0]

    return render(request, "index.html", context)


def register(request):
    context={}
    if request.method=="POST":
        #fetch data from html form
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        check = User.objects.filter(username=email)
        if len(check)==0:
            usr = User.objects.create_user(email, email, password)
            usr.first_name = name
            usr.save()

            
            context['status'] = f"User {name} Registered Successfully!"
        else:
            context['error'] = "A User with this email already exists"

        # check_user = authenticate(username=email, password=password)
        
        # login(request, check_user)
        # if check_user.is_superuser or check_user.is_staff:
        #     return HttpResponseRedirect('/admin')
        # return HttpResponseRedirect('/')
        
    return render(request,'register.html', context)


def signin(request):
    context={}
    if request.method=="POST":
        email = request.POST.get('email')
        passw = request.POST.get('password')

        check_user = authenticate(username=email, password=passw)
        
        if check_user:
            login(request, check_user)
            if check_user.is_superuser or check_user.is_staff:
                return HttpResponseRedirect('/admin')
            return HttpResponseRedirect('/')
        else:
            context.update({'message':'Invalid Login Details!','class':'alert-danger'})

    return render(request,'login.html', context)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url="/login/")
def post_ad(request):
    context={}
    cats = Category.objects.all().order_by('name')
    
    context['categories'] = cats
    if request.method=="POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        images = request.FILES.getlist("product_image")
        price = request.POST.get("price")
        contact = request.POST.get("contact")
        category_id = request.POST.get("category")
        condition = request.POST.get("condition")
        brand = request.POST.get("brand")
        
        category = Category.objects.filter(id=category_id).first()

        product = Product.objects.create(
            title = title,
            description = description,
            price = price,
            contact_number = contact,
            category = category,
            condition = condition,
            owner = request.user,
            brand = brand
        )

        product_images = []
        for image in images:
            product_images.append(ProductImage(product_id=product, product_image=image))
        
        ProductImage.objects.bulk_create(product_images)


    
        return redirect(f"/product/{product.slug}")

    return render(request, "post-ad.html", context)



def view_ad(request, slug):
    
    product = Product.objects.get(slug = slug)
    product_images = ProductImage.objects.filter(product_id=product)

    context = {}

    if request.method == "POST":
        data = request.POST

        contact = data.get('contact')
        price = data.get('price')


        BuyerPrice.objects.create(
            product_id = product,
            buyer = request.user,
            contact_number = contact, 
            price = price,
        )
        context['status'] = "Quote price submitted successfully"

    buyer = BuyerPrice.objects.filter(product_id=product)

    context["product"] = product
    context["buyers"] = buyer
    context["product_images"] = product_images

    return render(request, "view-ad.html", context)



def category_page(request, category_id):
    context = {}

    category = get_object_or_404(Category, id=category_id)
    products = Product.objects.filter(category=category)

    if request.user.is_authenticated:
        products = products.exclude(owner = request.user).values()
    else:
        products = products.values()

    images = ProductImage.objects.filter(product_id__category = category)

    product_images_dict = {}
    for i in images:
        if i.product_id.pk not in product_images_dict:
            product_images_dict[i.product_id.pk] = []
        product_images_dict[i.product_id.pk].append(i.product_image)
    
    

    for product in products:
        product["image"] = product_images_dict[product["id"]][0]
    
    
    context['category'] = category
    context['products'] = products

    return render(request, "categories.html", context)

        

def my_ads(request):

    context = {}
    products = Product.objects.filter(owner=request.user).values()

    images = ProductImage.objects.filter(product_id__owner = request.user)

    product_images_dict = {}
    for i in images:
        if i.product_id.pk not in product_images_dict:
            product_images_dict[i.product_id.pk] = []
        product_images_dict[i.product_id.pk].append(i.product_image)
    
    for product in products:
        product["image"] = product_images_dict[product["id"]][0]

    context['products'] = products

    return render(request, "myads.html", context)


def guide(request):
    return render(request, "guide.html")

def terms(request):
    return render(request, "terms.html")

def privacy(request):
    return render(request, "privacy.html")


    
        


    

