from django.urls import path,include
from . import views


urlpatterns = [
    path('create/',views.create_query,name = "create_query"),
    path('query/<slug:slug>/view/<int:pk>',views.QueryDetailView.as_view(),name = "query_detail_view")
    
]