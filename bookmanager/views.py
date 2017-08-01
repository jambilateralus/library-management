from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Book
from .serializers import CompleteBookSerializer, BookSerializer


class BookList(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer = CompleteBookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


