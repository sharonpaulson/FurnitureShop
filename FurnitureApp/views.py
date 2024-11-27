from django.shortcuts import render, redirect
from FurnitureApp.models import CategoryDB, ProductDB
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
import datetime
from WebApp.models import ContactDB


def index(request):
    x = datetime.datetime.now()
    cat = CategoryDB.objects.count()
    pro = ProductDB.objects.count()
    return render(request, 'index.html', {'x': x, 'cat': cat, 'pro': pro})


def add_categories(request):
    return render(request, "add_categories.html")


def save_categories(request):
    if request.method == "POST":
        category_name = request.POST.get('category_name')
        category_desc = request.POST.get('category_desc')
        category_image = request.FILES['category_image']
        obj = CategoryDB(Category_Name=category_name,
                         Category_Description=category_desc,
                         Category_Image=category_image)
        obj.save()
        messages.success(request, "New Category Added....!")
        return redirect(add_categories)


def display_categories(request):
    category = CategoryDB.objects.all()
    return render(request, "display_categories.html", {'category': category})


def edit_categories(request, cat_id):
    category = CategoryDB.objects.get(id=cat_id)
    return render(request, "edit_categories.html", {'category': category})


def update_categories(request, cat_id):
    if request.method == "POST":
        category_name = request.POST.get('category_name')
        category_desc = request.POST.get('category_desc')
        try:
            category_image = request.FILES['category_image']
            fs = FileSystemStorage()
            file = fs.save(category_image.name, category_image)

        except MultiValueDictKeyError:
            file = CategoryDB.objects.get(id=cat_id).Category_Image

        CategoryDB.objects.filter(id=cat_id).update(Category_Name=category_name,
                                                    Category_Description=category_desc,
                                                    Category_Image=file)
        messages.success(request, "Categories updated...!")

        return redirect(display_categories)


def delete_categories(request, cat_id):
    category = (CategoryDB.objects.filter(id=cat_id))
    category.delete()
    messages.error(request, "Category deleted....!")
    return redirect(display_categories)


def add_products(request):
    cat = CategoryDB.objects.all()
    return render(request, "add_products.html", {'cat': cat})


def save_products(request):
    if request.method == "POST":
        product_category = request.POST.get('product_category')
        product_name = request.POST.get('product_name')
        product_quantity = request.POST.get('product_quantity')
        product_mrp = request.POST.get('product_mrp')
        product_desc = request.POST.get('product_desc')
        product_country = request.POST.get('product_country')
        product_mfd = request.POST.get('product_mfd')
        product_image1 = request.FILES['product_image1']
        product_image2 = request.FILES['product_image2']
        product_image3 = request.FILES['product_image3']

        obj = ProductDB(
            Product_Category=product_category,
            Product_Name=product_name,
            Product_Quantity=product_quantity,
            Product_MRP=product_mrp,
            Product_Description=product_desc,
            Product_Country=product_country,
            Product_Mfd=product_mfd,
            Product_Image1=product_image1,
            Product_Image2=product_image2,
            Product_Image3=product_image3
        )
        messages.success(request, "New Product Added....!")
        obj.save()
        return redirect(add_products)


def display_products(request):
    pro = ProductDB.objects.all()
    return render(request, "display_products.html", {'pro': pro})


def edit_products(request, pro_id):
    cat = CategoryDB.objects.all()
    pro = ProductDB.objects.get(id=pro_id)
    return render(request, "edit_products.html", {'cat': cat, 'pro': pro})


def update_products(request, pro_id):
    if request.method == "POST":
        product_category = request.POST.get('product_category')
        product_name = request.POST.get('product_name')
        product_quantity = request.POST.get('product_quantity')
        product_mrp = request.POST.get('product_mrp')
        product_desc = request.POST.get('product_desc')
        product_country = request.POST.get('product_country')
        product_mfd = request.POST.get('product_mfd')
        try:
            product_image1 = request.FILES['product_image1']
            fs = FileSystemStorage()
            file1 = fs.save(product_image1.name, product_image1)

        except MultiValueDictKeyError:
            file1 = ProductDB.objects.get(id=pro_id).Product_Image1

        try:
            product_image2 = request.FILES['product_image2']
            fs = FileSystemStorage()
            file2 = fs.save(product_image2.name, product_image2)

        except MultiValueDictKeyError:
            file2 = ProductDB.objects.get(id=pro_id).Product_Image2

        try:
            product_image3 = request.FILES['product_image3']
            fs = FileSystemStorage()
            file3 = fs.save(product_image3.name, product_image3)

        except MultiValueDictKeyError:
            file3 = ProductDB.objects.get(id=pro_id).Product_Image3

        ProductDB.objects.filter(id=pro_id).update(Product_Category=product_category,
                                                   Product_Name=product_name,
                                                   Product_Quantity=product_quantity,
                                                   Product_MRP=product_mrp,
                                                   Product_Description=product_desc,
                                                   Product_Country=product_country,
                                                   Product_Mfd=product_mfd,
                                                   Product_Image1=file1,
                                                   Product_Image2=file2,
                                                   Product_Image3=file3)
        messages.success(request, "Products Updated...!")

        return redirect(display_products)


def delete_products(request, pro_id):
    pro = ProductDB.objects.filter(id=pro_id)
    pro.delete()
    messages.error(request, "Product Deleted...!")
    return redirect(display_products)


def admin1(request):
    return render(request, "admin.html")


def admin_login(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pw = request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un, password=pw)
            if x is not None:
                login(request, x)
                request.session['username'] = un
                request.session['password'] = pw
                messages.success(request, "Welcome..!")
                return redirect(index)
            else:
                messages.warning(request, "Wrong password..!")

                return redirect(admin1)
        else:
            messages.warning(request, "Invalid Username..!")

            return redirect(admin1)


def admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request, "Log out Success..!")

    return redirect(admin1)


def contact_data(request):
    contact = ContactDB.objects.all()
    return render(request, "contact_data.html", {'contact': contact})


def delete_contact(request, con_id):
    contact = ContactDB.objects.filter(id=con_id)
    contact.delete()
    return redirect(contact_data)



