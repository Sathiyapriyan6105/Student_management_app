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
