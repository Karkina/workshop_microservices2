from django.urls import path
from snippets import views

urlpatterns = [
    path('api/deal/getAll', views.snippet_list),
    path('api/deal/getById<int:pk>/', views.snippet_detail),

    path('api/deal/getByName=<name>/', views.snippet_detailByName),
    path('api/deal/getDealsNumber/', views.snippet_numberDeal),

]