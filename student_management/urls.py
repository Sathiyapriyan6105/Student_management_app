"""student_management URL Configuration

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
from xml.dom.minidom import Document
from django.conf import settings
from django.contrib import admin
from django.urls import path
from student_data_app import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name='home'),
    path('create/',views.create_view,name="Create"),
    path('studentdetails/<int:STD_id>/',views.displaydetails,name="display"),
    path('additional/',views.create_details_view,name="add"),
    path('delete/<id>',views.delete_view),
    path('',views.login_user,name="login"),
    path('register/',views.register,name="register"),
    path('logout/',views.logout_user,name="logout")

]

# if settings.DEBUG:  
#         urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  
