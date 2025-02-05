from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

urlpatterns=[
    path('', views.home_page, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.loginpage, name='login'),
    path('sign-out/', views.signout, name='sign-out'),
    path('kyc/', views.kyc_registration, name='kyc'),
    path('account-info/', views.account_info, name='info'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('transfer/', views.transfer_view, name="transfer_view")

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
