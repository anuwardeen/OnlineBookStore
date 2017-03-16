from .models import Author, Book
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def top_authors_and_works_rest(request):
    """
    Top 10 authors and there best works.
    """
    if request.method == "GET":

        authors = Author.objects.all().order_by('-total_books_sold')[:5]
        serializer= AuthorSerializer(authors, many=True)
        return Response(serializer.data, template_name="rest_framework/api.html")


# from rest_framework import status
# from django.shortcuts import render
# from rest_framework import generics
# from rest_framework.views import APIView
# from rest_framework import mixins
# from rest_framework import generics


# def top_authors_and_works(request):
#     authors = Author.objects.all().order_by('-total_books_sold')[:2]
#     books =[]
#     for author in authors:
#         books.append(Book.objects.filter(author=author).order_by('-no_of_copies_sold_till_date')[:4])
#     return render(request,"bookstore/top_authors_and_their_works.html",{"books":books})

#
# @api_view(['GET'])
# def authors_list_rest(request):
#     """
#         List all the authors, or create a new author.
#         """
#     authors = Author.objects.all()
#     serializer = AuthorSerializer(authors, many=True)
#     return Response(serializer.data,template_name="rest_framework/api.html")



# def top_authors_and_works(request):
#     """
#     Top 10 authors and their works, without rest.
#     """
#     authors = Author.objects.all()
#     books =Book.objects.all()
#     return render(request, "bookstore/top_authors_and_their_works.html", {"authors":authors,"books":books})
# @api_view(['GET'])
# def authors_work_rest(request, author_id):
#     """
#     List all the books of particular author.
#     """
#     books = Book.objects.filter(author=int(author_id))
#     if books:
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data)
#     else:
#         return Response(status=status.HTTP_204_NO_CONTENT)
#

# @api_view(['GET'])
# def books_list_rest(request):
#     """
#     List all the authors, or create a new author.
#     """
#     books = Book.objects.all()
#     serializer = BookSerializer(books, many=True)
#     return Response(serializer.data)
#
# #
#
# @api_view(['GET'])
# def top_ten_books_rest(request):
#     """
#     List top ten books of all time.
#     """
#     books = Book.objects.all().order_by('-ratings')[:10]
#     serializer = BookSerializer(books, many=True)
#     return Response(serializer.data)
#
#
# @api_view(['GET'])
# def author_of_the_year_rest(request,year):
#     """
#     List details of Author of the year.
#     """
#     top_rating = Book.objects.filter(published_year=int(year)).order_by('-ratings').values('ratings')[0]['ratings']
#     author_id = Book.objects.filter(published_year=int(year),ratings=top_rating).values('author')
#     print(author_id)
#     authors= Author.objects.filter(author_id__in=author_id)
#     print(authors)
#     serializer = AuthorSerializer(authors, many=True)
#     return Response(serializer.data)
#
#
# def authors_list(request):
#     """
#     List all the authors, or create a new author.
#     """
#     authors = Author.objects.all()
#     serializer = AuthorSerializer(authors, many=True)
#     return render(request, "bookstore/authors.html", {"serializer":serializer.data})
#
#
# def authors_work(request, author_id):
#     """
#     List all the books of particular author.
#     """
#     books = Book.objects.filter(author=int(author_id))
#     serializer = BookSerializer(books, many=True)
#     return render(request, "bookstore/books.html", {"serializer":serializer.data})
#
#
# def books_list(request):
#     """
#     List all the authors, or create a new author.
#     """
#     books = Book.objects.all()
#     serializer = BookSerializer(books, many=True)
#     return render(request, "bookstore/books.html", {"serializer":serializer.data})

