from django.shortcuts import render
from .models import Car, Review
from django.http import JsonResponse

def home(request):
    cars = Car.objects.all()
    first_review = Review.objects.first()
    return render(request, 'home.html', {'cars':cars, 'first_review':first_review})

def get_reviews(request):
    reviews = Review.objects.all()  # Получаем все отзывы
    reviews_data = [
        {
            'photo': review.photo.url,
            'text': review.text,
            'customer_name': review.customer_name,
            'city': review.city,
            'created_at': review.created_at.strftime('%d.%m.%Y'),
        }
        for review in reviews
    ]
    return JsonResponse(reviews_data, safe=False)