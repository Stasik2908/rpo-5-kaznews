from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Adv
from django.db.models import Q

def home_page(request):
    # Последние 4 новых поста для "горячих новостей"
    hot_posts = Post.objects.all().order_by('-created_at')[:4]
    # 6 случайных постов для блока "Вам может быть интересно"
    random_posts = Post.objects.all().order_by('?')[:6]
    # Последние 4 рекламы (с сортировкой по id или дате, если добавите поле)
    advs = Adv.objects.all().order_by('-id')[:4]
    context = {
        'hot_posts': hot_posts,
        'random_posts': random_posts,  # Изменили название
        'advs': advs
    }
    return render(request, "index.html", context)

def all_news_page(request):
    # Все новости, отсортированные по дате
    posts = Post.objects.all().order_by('-created_at')
    # Последние 4 рекламы
    advs = Adv.objects.all().order_by('-id')[:4]
    context = {
        'posts': posts,
        'advs': advs
    }
    return render(request, "all-news.html", context)


def news_by_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    posts = Post.objects.filter(category=category).order_by('-created_at')
    # Добавили рекламу
    advs = Adv.objects.all().order_by('-id')[:4]
    context = {
        'category': category,
        'posts': posts,
        'advs': advs
    }
    return render(request, "news-by-category.html", context)

def search_page(request):
    # Добавили рекламу даже на страницу поиска
    advs = Adv.objects.all().order_by('-id')[:4]
    context = {
        'advs': advs
    }
    return render(request, "search.html", context)

def search_results(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
    
    # Добавили рекламу
    advs = Adv.objects.all().order_by('-id')[:4]
    context = {
        'query': query,
        'results': results,
        'advs': advs
    }
    return render(request, "search-results.html", context)

def read_news_page(request, pk):
    # Текущий пост
    post = get_object_or_404(Post, pk=pk)
    # 4 поста из этой категории
    related_posts = Post.objects.filter(
        category=post.category
    ).exclude(
        pk=pk
    ).order_by('?')[:4]
    
    # Добавили рекламу
    advs = Adv.objects.all().order_by('-id')[:4]
    context = {
        'post': post,
        'related_posts': related_posts,  # Добавили похожие посты
        'advs': advs
    }
    return render(request, "read-news.html", context)