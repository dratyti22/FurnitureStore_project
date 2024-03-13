from django.shortcuts import render

from main.models import StocksIndex, BannerIndex


def index(request):
    text_stocks_index = StocksIndex.objects.all()
    banner_text = BannerIndex.objects.all()
    context = {
        "language": True,
        "currency": True,
        'title': 'Furea - Home',
        'text_stocks_index': text_stocks_index,
        'banner_text': banner_text,
    }
    return render(request, 'main/index.html', context)
