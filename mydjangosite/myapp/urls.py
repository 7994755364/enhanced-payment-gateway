from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name = 'index'),
    path('base/', views.Base, name = 'base'),
    path('view_product/', views.view_product, name = 'view_product'),
    path('signup/', views.buyer_reg, name = 'signup'),
    path('', views.login, name = 'login'),
    path('accounts/login/', views.login),
    path('view_profile/', views.view_profile, name = 'view_profile'),
    path('cart/<int:product_id>/', views.cart, name = 'cart'),
    path('view_cart/', views.view_cart, name = 'view_cart'),
    path('remove_cart/<int:product_id>/', views.remove_cart, name = 'remove_cart'),
    path('checkout/', views.checkout, name = 'checkout'),
    path('payment_page/', views.payment_page, name='payment_page'),
    path('process_payment/', views.process_payment, name='process_payment'),
    path('payment_confirmation/', views.payment_confirmation, name='payment_confirmation'),
    path('payment_failed/', views.payment_failed, name='payment_failed'),
    path('logout/', views.user_logout, name='logout'),
    path('verify_otp/', views.verify_otp, name='verify_otp'),
    path('home/', views.home, name = 'home'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
