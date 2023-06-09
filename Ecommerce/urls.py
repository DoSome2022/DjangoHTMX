"""Ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib import admin
# from django.urls import path ,include
# from django.contrib.auth import views
# from cart.views import add_to_cart , cart , checkout

# from core.views import shop , signup 
# from product.views import product


# urlpatterns = [
#     path('', include('core.urls')),
#     path('signup/', signup, name='signup'),
#     path('logout/', views.LogoutView.as_view(), name='logout'),
#     path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
#     path('shop/', shop ,name="shop"),
#     path('shop/<slug:slug>', product , name="product"),
#     path('cart/', cart, name='cart'),
#     path('cart/checkout/', checkout, name='checkout'),
#     path('add_to_cart/<int:product_id>/',add_to_cart,name='add_to_cart'),
#     path('admin/', admin.site.urls),
# ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path('cart/', include('cart.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)