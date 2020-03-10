from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Book
from.serializer import Book_Serializer

class Book_Details(APIView):
   def get(self, request):
        reg = Book.objects.all()
        print(reg)
        json_reg = Book_Serializer(reg, many=True)
        return Response(json_reg.data)

