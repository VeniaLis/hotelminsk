from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404



from django.shortcuts import render, redirect, get_object_or_404

from .forms import LoginForm, RegisterForm, HotelForm, EditHotelDescriptionForm, ReviewForm
from .models import Hotel, Review


@login_required
def add_hotel(request):
    if request.method == 'POST':
        form = HotelForm(request.POST)
        if form.is_valid():
            hotel = Hotel.objects.create(**form.cleaned_data)
            return redirect('hotel_detail', hotel.id)
    else:
        form = HotelForm()
        return render(request, 'form.html', {'form': form})


@login_required
def edit_hotel(request, hotel_id):
    if request.method == 'POST':
        form = EditHotelDescriptionForm(request.POST)
        if form.is_valid():
            hotel = get_object_or_404(Hotel, pk=hotel_id)
            hotel.description = form.cleaned_data["description"]
            hotel.save()
            return redirect('hotel_detail', hotel.id)
    else:
        form = EditHotelDescriptionForm()
        return render(request, 'form.html', {'form': form})


@login_required
def add_review(request, hotel_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            user = request.user
            hotel = get_object_or_404(Hotel, pk=hotel_id)
            Review.objects.create(hotel=hotel, user=user, **form.cleaned_data)
            return redirect('hotel_review_list', hotel.id)
    else:
        form = ReviewForm()
        return render(request, 'form.html', {'form': form})


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    user = request.user
    if review.user == user:
        review.delete()
        return redirect('hotel_review_list', review.hotel.id)
    return HttpResponse('You can delete only your reviews!')


@login_required
def edit_review(request, review_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            user = request.user
            review = get_object_or_404(Review, pk=review_id)
            if review.user == user:
                review.text = form.cleaned_data["text"]
                review.save()
                return redirect('hotel_review_list', review.hotel.id)
            return HttpResponse('You can edit only your reviews!')
    else:
        form = ReviewForm()
        return render(request, 'form.html', {'form': form})

def index(request):
    return render(request, 'index.html')


def hotel_detail(request, hotel_id):
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    return render(request, 'hotel_detail.html', {'hotel': hotel})


def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotel_list.html', {'hotels': hotels})

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("index")
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'form.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect("index")


def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return redirect("login_user")
        else:
            return HttpResponse('Invalid registration')
    else:
        form = RegisterForm()

        return render(request, "form.html", {"form": form})


def review_detail(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    return render(request, 'review_detail.html', {'review': review})


def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'review_list.html', {'reviews': reviews})

def hotel_review_list(request, hotel_id):
    reviews = Review.objects.filter(hotel=hotel_id)
    return render(request, 'review_list.html', {'reviews': reviews})