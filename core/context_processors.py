from order.models import BasketItem
from django.db.models import Q

def base_data(request):
    data = {}
    if request.user.is_authenticated:
        user_basket =  BasketItem.objects.filter(Q(basket_id__user_id = request.user), Q(basket_id__is_active = True)).all()

        total_price = 0

        if user_basket:
            data['user_basket'] = user_basket

            for product in user_basket:
                total_price += product.get_subtotal()
            data['total_price'] = total_price

    return data