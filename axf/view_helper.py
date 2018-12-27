from axf.models import Cart


def total_price(request):
    user_id=request.session.get('user_id')
    carts=Cart.objects.filter(user_id=user_id,ischoose=True)
    total=0
    for cart in carts:
        total+=cart.cart_num * cart.goods.price
    return total