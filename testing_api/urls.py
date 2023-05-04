from . import views
from django.urls import path 

urlpatterns = [
    path('', views.users_list, name="users"),
    path("snippets", views.snippet_list, name="snippets"),
    path("snippets/<int:pk>", views.snippets_detail, name="snippets_detail")
]
