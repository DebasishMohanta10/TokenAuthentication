from rest_framework import serializers
from .models import Book,Category
import bleach

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model =Category
        fields=('__all__')

    def validate(self,attrs):
        attrs['name'] = bleach.clean(attrs['name'])
        attrs['slug'] = bleach.clean(attrs['name'])
        return super().validate(attrs)


class BooksSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source='inventory')
    category = CategorySerializer(many=True,read_only=True)
    category_ids = serializers.ListField(write_only=True)
    class Meta:
        model =Book
        fields=['id','name','author','price','stock','category','category_ids']

    def create(self, validated_data):
        category_ids = validated_data.pop('category_ids',[])
        book = Book.objects.create(**validated_data)

        for category_id in category_ids:
            category = Category.objects.get(pk=category_id)
            book.category.add(category)
        return book

    def validate(self,attrs):
        attrs['name'] = bleach.clean(attrs['name'])
        attrs['author'] = bleach.clean(attrs['author'])
        if attrs['price'] < 10:
            raise serializers.ValidationError("Book Price Must be Greater than 10")
        if attrs['inventory'] <= 0:
            raise serializers.ValidationError('Stock must be greater then zero')
        return super().validate(attrs)

