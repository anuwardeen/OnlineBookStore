from rest_framework import serializers
from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"



class AuthorSerializer(serializers.ModelSerializer):

    books = serializers.SerializerMethodField()

    class Meta:

        model = Author
        fields = ("author_id","author_name","author_email_id","books")
        # fields = "__all__"

    @staticmethod
    def get_books(obj):
        book_list = Book.objects.filter(author=obj).order_by('-no_of_copies_sold_till_date')[:2]
        serializer = BookSerializer(book_list, many=True)
        return serializer.data
