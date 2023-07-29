from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('books/',views.BooksView.as_view()),
    path('books/<int:pk>',views.SingleBookView.as_view()),
    path('categories/',views.CategoryView.as_view()),
    path("secret/",views.secret),
    path("obtain-auth-token/",obtain_auth_token)
]

