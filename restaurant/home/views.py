from django.shortcuts import render
from meals.models import Meals, Category
from blog.models import Post
from django.core.paginator import Paginator
from aboutus.models import Why_Choose_Us

# Create your views here.
def home(request):
    meals = Meals.objects.all()
    meal_list = Meals.objects.all()
    categories = Category.objects.all()
    posts = Post.objects.all()
    latest_post = Post.objects.last()
    why_choose_us = Why_Choose_Us.objects.all()
    post_list = Post.objects.all()


   #pagination meals
    paginator = Paginator(meals, 6)
    page_number = request.GET.get('page')
    meals = paginator.get_page(page_number)

    #pagination blog
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page')
    post_list = paginator.get_page(page_number)

    context = {
          'meals' : meals,
          'meal_list' : meal_list ,
          'categories' : categories ,
          'posts' : posts ,
          'latest_post' : latest_post ,
          'why_choose_us' : why_choose_us ,
          'post_list':post_list,
          
    }
    return render(request , 'home/index.html',context)