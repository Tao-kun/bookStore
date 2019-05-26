from django.http import JsonResponse
from django.shortcuts import render
from watch_buy import models as watch_buy_models
import datetime
import time
# Create your views here.


def see_order(request):
    stu_id = request.session.get('studentID')
    all_order = watch_buy_models.Order.objects.filter(user_id=stu_id)
    for order in all_order:
        order_datetime = order.orderdate
        if order.IsHandled == 0:
            timenow = time.mktime(datetime.datetime.now().timetuple())
            timeord = time.mktime(order_datetime.timetuple())
            diff = timenow - timeord
            if float(diff) / 3600000 >= 0.5:
                order.IsCancle = 1
                order.save()
    return render(request, "after_sold/Order.html", locals())


def order_detail(request):
    order_id = request.GET.get("order_id")
    order_info = watch_buy_models.Order.objects.get(orderid=order_id)

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


def confirm_order(request):
    id = request.GET.get('order_id')
    order_obj = watch_buy_models.Order.objects.get(orderid=id)
    order_obj.IsHandled = 1
    order_obj.save()
    return render(request, "after_sold/confirm_order.html", locals())


def confirm_receive(request):
    id = request.GET.get('order_id')
    response = JsonResponse({"info": "成功收货"})
    order_obj = watch_buy_models.Order.objects.get(orderid=id)
    if order_obj.IsShipped == 1 and order_obj.IsCancled == 0:       #   已发货但是没有被取消
        order_obj.IsCompleted = 1
        order_obj.save()
    else:
        response = JsonResponse({"info": "收货失败"})
    return response


def calcel_order(request):
    id = request.GET.get('order_id')
    response = JsonResponse({"info": "成功取消订单"})
    order_obj = watch_buy_models.Order.objects.get(orderid=id)
    if order_obj.IsShipped == 0:
        order_obj.IsCancle = 1
        order_obj.save()
    else:
        response = JsonResponse({"info": "已发货，无法取消"})
    return response


def apply_return(request):
    id = request.GET.get('order_id')
    response = JsonResponse({"info": "已通知管理员"})
    order_obj = watch_buy_models.Order.objects.get(orderid=id)
    if order_obj.IsShipped == 1 and order_obj.IsCompleted == 0:
        order_obj.IsReturn = 1
        order_obj.save()
    else:
        response = JsonResponse({"info": "您已签收，恕不退货"})
    return response


def comment_order(request):
    id = request.GET.get('order_id')
    comment = request.GET.get('comment')
    response = JsonResponse({"info": "评价成功"})
    order_obj = watch_buy_models.Order.objects.get(orderid=id)
    if order_obj.IsCompleted == 1:
        order_obj.Comment = comment
        order_obj.save()
    else:
        response = JsonResponse({"info": "未签收，无法评价"})
    return response


def cancel_return(request):
    id = request.GET.get('order_id')
    response = JsonResponse({"info": "取消成功"})
    order_obj = watch_buy_models.Order.objects.get(orderid=id)
    if order_obj.IsReturn == 1 and order_obj.IsCancled == 0:
        order_obj.IsCompleted = 1
        order_obj.save()
    else:
        response = JsonResponse({"info": "取消失败"})
    return response

