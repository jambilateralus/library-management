from rest_framework import serializers

from .models import (
    Category,
    Publisher,
    Author,
    Book,
    BookCopy
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class CompleteBookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)
    publisher = PublisherSerializer()
    category = CategorySerializer()

    class Meta:
        model = Book
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class BookCopySerializer(serializers.ModelSerializer):
    book = CompleteBookSerializer()

    class Meta:
        models = BookCopy
        fields = '__all__'
