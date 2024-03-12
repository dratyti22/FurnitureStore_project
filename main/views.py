from django.shortcuts import render

from main.models import StocksIndex


def index(request):
    text_stocks_index = StocksIndex.objects.all()
    context = {
        "language": True,
        "currency": True,
        'title': 'Furea - Home',
        'text_stocks_index':text_stocks_index,
    }
    return render(request, 'main/index.html', context)
