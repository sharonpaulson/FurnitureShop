from django.urls import path
from WebApp import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('product_page/', views.product_page, name='product_page'),
    path('about_us/', views.about_us, name='about_us'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('save_contact/', views.save_contact, name='save_contact'),
    path('single_product/<int:pro_id>/', views.single_product, name='single_product'),

    path('products_filtered/<cat_name>/', views.products_filtered, name='products_filtered'),

    path('sign_up/', views.sign_up, name='sign_up'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('save_signup/', views.save_signup, name='save_signup'),
    path('', views.login_home, name='login_home'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('save_cart/', views.save_cart, name='save_cart'),
    path('cart_page/', views.cart_page, name='cart_page'),
    path('checkout/', views.checkout, name='checkout'),
    path('save_checkout/', views.save_checkout, name='save_checkout'),
    path('delete_cart<int:cart_id>/', views.delete_cart, name='delete_cart'),
    path('payment_page', views.payment_page, name='payment_page'),

]
