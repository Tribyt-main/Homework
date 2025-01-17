# Create your views here.

from django.shortcuts import render


# Create your views here.

def shop_page(request):
    games = {'games': ["Atomic Heart", "Cyberpunk 2077", "PayDay 2"]}
    list_games = games.get('games')
    context = {
        'list_games': list_games
    }
    return render(request, 'fourth_task/shop_page.html', context)


def main_page_task4(request):
    return render(request, 'fourth_task/main_page_task4.html')


def basket_page(request):
    return render(request, 'fourth_task/basket_page.html')
