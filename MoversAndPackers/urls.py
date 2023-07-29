"""MoversAndPackers URL Configuration

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
from django.contrib import admin
from django.urls import path
from moverspackers.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='index'),
    path('admin_login',admin_login,name='admin_login'),
    path('admin_home',admin_home,name='admin_home'),
    path('add_services',add_services,name='add_services'),
    path('manage_services',manage_services,name='manage_services'),
    path('edit_service/<int:pid>',edit_service, name='edit_service'),
    path('delete_service/<int:pid>',delete_service, name='delete_service'),
    path('/logout',Logout, name='logout'),
    path('services',services,name='services'),
    path('about', about, name='about'),
    path('request_quote',request_quote,name='request_quote'),
    path('new_booking',new_booking, name='new_booking'),
    path('view_bookingdetail/<int:pid>',view_bookingdetail, name='view_bookingdetail'),
    path('old_booking', old_booking, name='old_booking'),
    path('contact',contact, name='contact'),
    path('read_queries',read_queries, name='read_queries'),
    path('unread_queries',unread_queries, name='unread_queries'),
    path('view_queries/<int:pid>',view_queries, name='view_queries'),
    path('delete_queries/<int:pid>', delete_queries, name='delete_queries'),
    path('search',search, name='search'),
path('change_passwordadmin',change_passwordadmin, name='change_passwordadmin'),
    path('betweendate_bookingreport',betweendate_bookingreport, name='betweendate_bookingreport'),
path('betweendate_contactreport',betweendate_contactreport, name='betweendate_contactreport'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


