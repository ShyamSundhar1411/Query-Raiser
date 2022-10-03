from django.urls import path,include
from . import views


urlpatterns = [
    path('create/',views.create_query,name = "create_query"),
    
]