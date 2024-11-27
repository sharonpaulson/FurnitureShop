import razorpay
from django.shortcuts import render, redirect
from FurnitureApp.models import ProductDB, CategoryDB
from WebApp.models import ContactDB, SignupDB, CartDB, OrderDB
from django.contrib import messages


def home(request):
    cart = CartDB.objects.filter(Username=request.session['Signup_Name'])
    x = cart.count()
    categories = CategoryDB.objects.all()
    return render(request, "home.html", {'categories': categories, 'x': x})


def product_page(request):
    cart = CartDB.objects.filter(Username=request.session['Signup_Name'])
    x = cart.count()
    products = ProductDB.objects.all()
    return render(request, "product_page.html", {'products': products, 'x': x})


def about_us(request):
    return render(request, "about_us.html")


def contact_us(request):
    return render(request, "contact_us.html")


def save_contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        message = request.POST.get('message')
        obj = ContactDB(Name=name, Mobile=mobile, Email=email, Message=message)
        obj.save()
        messages.success(request, "Contact saved...!")
        return redirect(contact_us)


def products_filtered(request, cat_name):
    data = ProductDB.objects.filter(Product_Category=cat_name)
    return render(request, "products_filtered.html", {'data': data})


def single_product(request, pro_id):
    pro = ProductDB.objects.get(id=pro_id)
    return render(request, 'single_product.html', {'pro': pro})


def sign_up(request):
    return render(request, "sign_up.html")


def save_signup(request):
    if request.method == "POST":
        name = request.POST.get('username')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if SignupDB.objects.filter(Signup_Name=name).exists():
            messages.warning(request, "User already exists..!")
            return redirect(sign_up)

        elif SignupDB.objects.filter(Signup_Email=email).exists():
            messages.warning(request, "Email is already linked with another account..!")
            return redirect(sign_up)
        obj = SignupDB(Signup_Name=name, Signup_Email=email, Signup_Mobile=mobile, Signup_Password=password,
                       Signup_ConfirmPassword=confirm_password)

        obj.save()

        return redirect(sign_in)


def sign_in(request):
    return render(request, "sign_in.html")


def login_home(request):
    if request.method == "POST":
        un = request.POST.get('user')
        pw = request.POST.get('pass')
        if SignupDB.objects.filter(Signup_Name=un, Signup_Password=pw).exists():
            request.session['Signup_Name'] = un
            request.session['Signup_Password'] = pw
            messages.success(request, "Welcome back...!")

            return redirect(home)
        else:
            messages.error(request, "Wrong Password...!")

            return redirect(sign_in)
    else:
        messages.warning(request, "Invalid Username...!")

        return redirect(sign_in)


def user_logout(request):
    del request.session['Signup_Name']
    del request.session['Signup_Password']
    return redirect(sign_in)


def save_cart(request):
    if request.method == "POST":
        username = request.POST.get('username')
        product_name = request.POST.get('product_name')
        product_quantity = request.POST.get('product_quantity')
        total_price = request.POST.get('total_price')
        try:
            x = ProductDB.objects.get(Product_Name=product_name)
            img = x.Product_Image1
        except ProductDB.DoesNotExist:
            img = None
        obj = CartDB(Username=username, Product_Name=product_name, Product_Quantity=product_quantity,
                     Total_Price=total_price, Product_Image=img)
        obj.save()
        return redirect(cart_page)


def cart_page(request):
    cart = CartDB.objects.filter(Username=request.session['Signup_Name'])
    x = cart.count()
    subtotal = 0
    shipping_charge = 0
    total = 0
    for i in cart:
        subtotal += i.Total_Price
        if subtotal > 200000:
            shipping_charge = 4000
        else:
            shipping_charge = 1000
        total = subtotal + shipping_charge

    return render(request, "cart_page.html", {'cart': cart, 'subtotal': subtotal,
                                              'shipping_charge': shipping_charge, 'total': total, 'x': x})


def delete_cart(request, cart_id):
    cart = CartDB.objects.filter(id=cart_id).delete()
    return redirect(cart_page)


def checkout(request):
    cart = CartDB.objects.filter(Username=request.session['Signup_Name'])
    subtotal = 0
    shipping_charge = 0
    total = 0
    for i in cart:
        subtotal += i.Total_Price
        if subtotal > 200000:
            shipping_charge = 4000
        else:
            shipping_charge = 1000
        total = subtotal + shipping_charge
    return render(request, "checkout.html", {'cart': cart, 'subtotal': subtotal,
                                             'shipping_charge': shipping_charge, 'total': total})


def save_checkout(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        place = request.POST.get('place')
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')
        message = request.POST.get('message')
        total = request.POST.get('total')
        obj = OrderDB(Name=name, Email=email, Place=place, Address=address, Mobile=mobile,
                      Message=message, TotalPrice=total)
        obj.save()
        return redirect(payment_page)


def payment_page(request):
    # Retrieve the data from OrderDB with the specified ID
    customer = OrderDB.objects.order_by('-id').first()

    # Get the payment amount of the specified customer
    pay = customer.TotalPrice

    # Convert the payment from rupees to paisa
    amount = int(pay * 100)

    pay_str = str(amount)

    for i in pay_str:
        print(i)
    if request.method == "POST":
        currency = 'INR'
        client = razorpay.Client(auth=('rzp_test_lNXSDhZZVv1D2w', 'cuz4W894VqoZG1MeD72YrKCp'))
        payment = client.order.create({'amount': amount, 'currency': currency})

    return render(request, "payment_page.html", {'customer': customer, 'pay_str': pay_str})
