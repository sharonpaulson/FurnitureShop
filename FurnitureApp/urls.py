from django.urls import path
from FurnitureApp import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('add_categories/', views.add_categories, name='add_categories'),
    path('save_categories/', views.save_categories, name='save_categories'),
    path('display_categories/', views.display_categories, name='display_categories'),

    path('edit_categories/<int:cat_id>/', views.edit_categories, name='edit_categories'),
    path('update_categories/<int:cat_id>/', views.update_categories, name='update_categories'),
    path('delete_categories/<int:cat_id>/', views.delete_categories, name='delete_categories'),

    path('add_products/', views.add_products, name='add_products'),
    path('save_products/', views.save_products, name='save_products'),
    path('display_products/', views.display_products, name='display_products'),

    path('edit_products/<int:pro_id>/', views.edit_products, name='edit_products'),
    path('update_products/<int:pro_id>/', views.update_products, name='update_products'),


    path('admin1/', views.admin1, name='admin1'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),


    path('contact_data/', views.contact_data, name='contact_data'),
    path('delete_contact/<int:con_id>/', views.delete_contact, name='delete_contact'),


]
