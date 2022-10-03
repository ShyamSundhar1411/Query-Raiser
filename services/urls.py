from django.urls import path,include
from . import views


urlpatterns = [
    path('',views.home,name = "portal"),
    path('create/',views.create_query,name = "create_query"),
    path('query/<slug:slug>/view/<int:pk>/',views.QueryDetailView.as_view(),name = "query_detail_view"),
    path('query/<int:pk>/view/<slug:slug>/approve/',views.approve_query,name = "approve_query"),
    path('query/<int:pk>/view/<slug:slug>/reject/',views.reject_query,name = "reject_query"),
    path('profile/<slug:slug>/view/',views.profile,name = "profile")
    
]