from rest_framework import generics
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from .models import User, Book
from .serializer import UserSerealizer, BookSerealizer

# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerealizer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def book_create(request):
    title = request.POST.get('title', False)
    description = request.POST.get('description' ,False)
    if not (title and description):
        content = {
            'status' : False,
            'message' : 'title and description are required'
        }
        return Response(content)
    book = Book.objects.create(title=title, description=description)
    serializer = BookSerealizer(book).data
    content = {
        'status' : True,
        'message' : 'book created successfully',
        'book' : serializer
    }

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def book_retrive(request):
    books = Book.objects.all()
    serializer = BookSerealizer(books, many=True).data
    content = {
        'status' : True,
        'books' : serializer
    }

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def book_update(request):
    id = request.PUT.get('id', False)
    title = request.PUT.get('title', False)
    description = request.PUT.get('description' ,False)
    if not id:
        content = {
            'status' : False,
            'message' : 'id is required'
        }
        return Response(content)
    book = Book.objects.filter(id=id)
    if not title:
        title = book[0].title
    if not description:
        description = book[0].description
    book = book.update(title=title, description=description)
    serializer = BookSerealizer(book).data
    content = {
        'status' : True,
        'message' : 'book updated successfully',
        'book' : serializer
    }
    return Response(content)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def book_delete(request):
    id = request.DELETE.get('id', False)
    book = Book.objects.filter(id=id)
    if not book:
        content = {
            'status' : False,
            'meassage' : 'book does not exist'
        }
        return Response(content)
    book.delete()
    content = {
            'status' : True,
            'meassage' : 'book deleted successfully'
        }
    return Response(content)