from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.auth_login, name='auth_login'),
    path('logout', views.auth_logout, name='auth_logout'),
    path('home', views.home, name='home'),
    path('categories/<str:category>', views.productcategory, name='productcategory'),
    path('products/<int:pid>', views.productdetail, name='productdetail'),
    path('updateproducts', views.updateform, name='updateform'),
    path('addproduct', views.addproduct, name="addproduct"),
    path('deleteproduct', views.deleteproduct, name='deleteproduct'),
]