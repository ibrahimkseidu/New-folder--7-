 def average_rating(rating_list):
 if not rating_list:
 return 0
 return round(sum(rating_list) / len(rating_list))
 from django.shortcuts import render, get_object_or_404
 from .models import Book
 from .utils import average_rating
 def index(request):
 return render(request, "base.html")
 def book_search(request):
 search_text = request.GET.get("search", "")
 return render(request,
 "reviews/search-results.html",
 {"search_text": search_text})