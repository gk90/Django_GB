from basketapp.models import Basket


def basket(request):
    basket = []

    if request.user.is_authenticated:
        basket = Basket.get_items(request.user)

    return {'basket': basket}
