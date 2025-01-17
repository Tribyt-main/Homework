from django.shortcuts import render


# Create your views here.
def shop_page(request):
    games = {
        "Atomic Heart": "Купить",
        "Cyberpunk 2077": "Купить",
        "PayDay 2": "Купить"
    }
    return render(request, 'third_task/shop_page.html', {'games': games})


def main_page_task3(request):
    return render(request, 'third_task/main_task3.html')


def basket_page(request):
    return render(request, 'third_task/basket_page.html')
