from django.contrib import admin
from django.urls import path,include
from . import views #importing views folder to declare the functions calls
 #path('<endpoint name i.e http://127.0.0.1:8000/hello>',<views.function name>)
  #path('',<views.function name>) if nothing is given in the endpoint name, then the changes are done to the home page
urlpatterns = [
    path('hello',views.helloworld)  , 
    path('',views.home_page),
    path('all-analytics',views.all_analytics),
    path('<slug:customname>',views.redirect_url)
]
