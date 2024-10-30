from .serializer import BookSerializer, AuthorSerializer
from .models import Book, Author
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class AuthorListAPI(APIView):
    def get(self, request):
        author = Author.objects.all()
        serializer = AuthorSerializer(author, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = AuthorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "status": "OK",
                "message": "Malumot saqlandi"
            }
            return Response(data)
        else:
            data = {
                "status": "Failed",
                "message": "Malumot saqlanmadi"
            }
        return Response(data)


class AuthorDetail(APIView):
    def authorni_olish(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            return Response(status=404)

    def get(self, request, pk):
        author = self.authorni_olish(pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    def put(self, request, pk):
        author = self.authorni_olish(pk)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        author = self.authorni_olish(pk)
        author.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BookListAPI(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            data = {
                "status": "OK",
                "message": "Malumot saqlandi"
            }
            return Response(data)
        else:
            data = {
                "status": "Failed",
                "message": "Malumot saqlanmadi"
            }
        return Response(data)


class BookDetail(APIView):
    def bookni_olish(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response(status=404)

    def get(self, request, pk):
        book = self.bookni_olish(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        book = self.bookni_olish(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = self.bookni_olish(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class AuthorListCreateAPI(generics.ListCreateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#
#
# class AuthorDetailUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#
#
# class BookListCreateAPI(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class BookDetailUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#

# class BookRetrieveUpdateAPI(generics.RetrieveUpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class BookDeleteRetrieveAPI(generics.RetrieveDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# class BookListAPI(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# class BookDetailAPI(generics.RetrieveAPIView):
#     #lookup_field = "id"
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class BookUpdateAPI(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class BookCreateAPI(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class BookDeleteAPI(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
