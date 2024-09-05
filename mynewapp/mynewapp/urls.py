from django.contrib import admin
from django.urls import path, include
from myapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('myapp.urls')),
    path('app2/', include('myapp2.urls')),
    path('', include('myapp.urls')),  # This handles the root URL
    path('myfirstpage',views.myfirstpage,name='myfirstpage'),
    path('mysecondpage',views.mysecondpage,name='mysecondpage'),
    path('mythirdpage',views.mythirdpage,name='mythirdpage'),
    path('myimagepage',views.myimagepage,name='myimagepage'),
    path('myform',views.myform,name='myform')

]
