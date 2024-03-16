from django.shortcuts import render

from main.models import StocksIndex, BannerIndex, PopularItemsTitle, PopularItems, PopularItemsProduct, SocialNetwork


def index(request):
    text_stocks_index = StocksIndex.objects.all()
    banner_text = BannerIndex.objects.all()
    popular_item_title = PopularItemsTitle.objects.all()
    popular_items = PopularItems.objects.all()
    popular_items_product = PopularItemsProduct.objects.all()
    social_network = SocialNetwork.objects.all()
    context = {
        "language": True,
        "currency": True,
        'title': 'Furea - Home',
        'text_stocks_index': text_stocks_index,
        'banner_text': banner_text,
        'popular_item_title': popular_item_title,
        'popular_items': popular_items,
        'popular_items_product': popular_items_product,
        'social_network': social_network,
    }
    return render(request, 'main/index.html', context)
