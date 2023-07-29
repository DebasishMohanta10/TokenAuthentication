# TokenAuthentication
Implement Token Authentication using DRF

- URL Routing

```
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

```

- Settings

```
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework.renderers.JSONRenderer'
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
        'rest_framework.filters.SearchFilter',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS' : 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 5
}
```

- Views
```
@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({"message": "This is the secret message for Authenticated user"})
```
