"""
URL configuration for passwordmanager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from passwordmanager import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='home'),
    path('login/',views.loginPage, name='login'),
    path('signup/',views.signup, name='signup'),
    path('logout/',views.logoutPage,name='logout'),
    path('create-database/',views.creatDb, name='dbcreate'),
    path('update-database/<id>',views.updateDb, name='dbupdate'),
    path('delete-database/<id>',views.deleteDb, name='dbdelete'),
    path('password/<id>',views.viewPassword, name='password.view'),
    path('password-create/<id>',views.createPassword, name='password.creat'),
    path('password-update/<id>',views.updatePassword, name='password.update'),
    path('password-delete/<id>',views.deletePassword, name='password.delete')



]
