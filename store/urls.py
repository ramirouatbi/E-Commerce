from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name = "store"),
    path('cart/', views.cart, name = "cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('contact/', views.contact, name="contact"),
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('contact/store/contact', views.contact, name="contactt"),
    path('products/<slug>', views.single, name="single"),
    path('cart/<slug>', views.update_cart, name="update_cart"),
]