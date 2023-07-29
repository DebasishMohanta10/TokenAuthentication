from django.shortcuts import render
from rest_framework import generics
from .models import Book,Category
from .serializers import BooksSerializer,CategorySerializer
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class BooksView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer
    ordering_fields = ['price','inventory']
    search_fields = ['category__name','name']
    filterset_fields = ['category']

class SingleBookView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BooksSerializer

@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({"message": "This is the secret message for Authenticated user"})
