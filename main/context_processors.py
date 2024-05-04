from .models import Basket


def get_total_amount(request):
    if request.user.is_authenticated:
        current_user = request.user
        baskets = Basket.objects.filter(user_name=current_user, is_complete=0)
        total = 0
        for i in baskets:
            total += i.amount
    else:
        total = 0
    return {'total_amount_all': total}
