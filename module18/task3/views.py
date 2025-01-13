from django.shortcuts import render


# Create your views here.
def shop_page(request):
    return render(request, 'shop_page.html')


def main_page_task3(request):
    return render(request, 'main_task3.html')


def basket_page(request):
    return render(request, 'basket_page.html')
