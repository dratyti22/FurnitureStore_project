from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank

from app.goods.models import Product


def q_search(query):
    search_vector = SearchVector(
        'description', weight='B') + SearchVector('name', weight='A')
    search_query = SearchQuery(query)
    return (Product.objects.annotate(rank=SearchRank(search_vector, search_query)).filter(rank__gte=0.5).order_by('-rank'))
