from django.urls import path
from snippets import views

urlpatterns = [
    path('snippets/', views.snippet_list),
    path('snippets/<int:pk>/', views.snippet_detail),

    path('snippets/name=<name>/', views.snippet_detailByName),
    path('snippets/dealsNumber/', views.snippet_numberDeal),

]