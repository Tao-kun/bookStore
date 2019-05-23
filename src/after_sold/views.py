from django.shortcuts import render
from watch_buy import models as watch_buy_models
# Create your views here.


def see_order(request):
    stu_id = request.session.get('studentID')
    all_order = watch_buy_models.Order.objects.filter(user_id=stu_id)
    return render(request, "after_sold/Order.html", locals())


def order_detail(request):
    order_id = request.GET.get("order_id")
    order_info = watch_buy_models.Order.objects.get(orderid=order_id)
    # print(order_id)
    class Goodrtn:
        def __init__(self, good, goodpic, qty):
            self.good = good
            self.goodpic = goodpic
            self.qty = qty
    goodrtnlist = []
    order_goods = watch_buy_models.OrderGood.objects.filter(order_id=order_id)
    for i in range(0, len(order_goods)):
        ISBN = order_goods[i].good_id
        good = watch_buy_models.Goods.objects.get(GoodISBN=ISBN)
        pic = watch_buy_models.GoodsPic.objects.filter(GoodISBN_id=ISBN)
        goodrtnlist.append(Goodrtn(good, pic[0], order_goods[i].count))
    return render(request, "after_sold/order_detail.html", locals())