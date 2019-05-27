import json

from django.shortcuts import render, redirect
from django.utils import timezone

import watch_buy.models as watch_buy_models
import login_manage.models as login_manage_models
# Create your views here.


# 显示商品列表
# 返回此商品的一张图以及商品的相关信息
def catalog_grid(request):
    if not request.session.get('studentID'):
        request.session.flush()
        return redirect('/login/')
    type = request.GET.get('type')
    if type is None:
        rtn_list = watch_buy_models.Goods.objects.all()
    else:
        rtn_list = watch_buy_models.Goods.objects.filter(Category=type)
    for rtn in rtn_list:
        rtn.GoodPrice = rtn.GoodPrice * rtn.GoodDiscount
    rtn_pic = []

    page_str = request.GET.get('page')
    if page_str is None:
        page = 1
    else:
        page = int(page_str)
    for i in range((page - 1) * 10, min(len(rtn_list), (page - 1) * 10 + 10)):
        GoodID = rtn_list[i].GoodISBN
        pic_tmp = watch_buy_models.GoodsPic.objects.filter(GoodISBN_id=GoodID)
        rtn_pic.append(pic_tmp[0])
    rtn_dic = dict(map(lambda x, y: [x, y], rtn_pic, rtn_list))
    return render(request, "watch_buy/catalog_grid.html", locals())


# 结账
def checkout(request):
    if not request.session.get('studentID'):
        request.session.flush()
        return redirect('/login/')
    good_name = request.GET.get("good_name")
    good_price = request.GET.get("good_price")
    good_json = request.GET.get("jsonData")     # 如果说是从购物车里边选择了多个商品,返回一个json对象
    studentID = request.session.get('studentID')
    default_info = login_manage_models.User.objects.get(studentID=studentID)

    class Good:
        def __init__(self, good_name, good_price, good_qty):
            self.good_name = good_name
            self.good_price = good_price
            self.good_qty = good_qty
    good_list = []
    count = 0
    sum_price = 0
    if good_json is not None:
        good_dic = json.loads(good_json)
        # 把所有的图书的信息存在list里，之后返回到checkout页面的列表中
        while count < (len(good_dic)/3):
            good_list.append(Good(good_dic[("book_name" + str(count))].replace("%", "\\").encode('utf-8').decode('unicode_escape'), good_dic["book_price" + str(count)], good_dic["book_qty" + str(count)]))
            sum_price += float(good_dic["book_price" + str(count)]) * float(good_dic["book_qty" + str(count)])
            count += 1
    else:
        good_list.append(Good(good_name, good_price, 1))
        sum_price = good_price
    cart_all = watch_buy_models.Cart.objects.filter(studentID_id=studentID)
    for cart_obj in cart_all:
        cart_obj.delete()
    print(sum_price)
    return render(request, "watch_buy/checkout.html", locals())


# 查看购物车
def shopping_cart(request):
    if not request.session.get('studentID'):
        request.session.flush()
        return redirect('/login/')
    studentID = request.session.get('studentID')
    good_num_list = watch_buy_models.Cart.objects.filter(studentID_id=studentID)

    class rtn:
        def __init__(self, pic, info, qty, id, sum):
            self.pic = pic
            self.info = info
            self.qty = qty
            self.id = id
            self.sum = sum

    rtn_list = []
    studentID = request.session.get('studentID')
    Total_sum = 0
    for i in range(len(good_num_list)):
        GoodID = good_num_list[i].GoodID_id
        pic_tmp = watch_buy_models.GoodsPic.objects.filter(GoodISBN_id=GoodID)
        info_tmp = watch_buy_models.Goods.objects.get(GoodISBN=GoodID)
        info_tmp.GoodPrice *= info_tmp.GoodDiscount
        Qty_tmp = watch_buy_models.Cart.objects.get(GoodID_id=GoodID, studentID_id=studentID)
        sum = Qty_tmp.Qty*info_tmp.GoodPrice
        re = rtn(pic_tmp[0], info_tmp, Qty_tmp.Qty, Qty_tmp.id, sum)
        Total_sum += sum
        rtn_list.append(re)
    return render(request, "watch_buy/shopping_cart.html", locals())


# 加入购物车
# 如果购物车里有这个商品,那么添加数量
# 否则新增记录
def add_to_cart(request):
    good_name = request.GET.get("good_name")
    good_price = request.GET.get("good_price")
    good_pic = request.GET.get("good_pic")
    good_ISBN = watch_buy_models.Goods.objects.get(GoodName=good_name).GoodISBN
    qty = 1
    try:
        qty = int(request.GET.get('qty'))
    except:
        qty = 1
    studentID = request.session.get('studentID')
    new_good = watch_buy_models.Goods.objects.get(GoodISBN=good_ISBN)
    new_stu = login_manage_models.User.objects.get(studentID=studentID)
    flag = watch_buy_models.Cart.objects.filter(GoodID_id=good_ISBN, studentID_id=studentID)
    if not flag:
        new_cart = watch_buy_models.Cart()
        new_cart.GoodID = new_good
        new_cart.studentID = new_stu
        new_cart.Qty = qty
        new_cart.save()
    else:
        new_cart = flag[0]
        new_cart.Qty = new_cart.Qty + qty
        new_cart.save()
    return render(request, "watch_buy/add_to_cart.html", locals())


# 查看商品详细信息
def good_detail(request):
    Good_ISBN = request.GET.get('ISBN')
    Good = watch_buy_models.Goods.objects.get(GoodISBN=Good_ISBN)
    Good.GoodPrice = Good.GoodPrice * Good.GoodDiscount
    Good_pic_list = watch_buy_models.GoodsPic.objects.filter(GoodISBN_id=Good_ISBN)
    return render(request, "watch_buy/product_page.html", locals())


# 添加订单
# name + "&address=" + address + "&zipcode=" + zipcode + "&telephone=" + telephone + "&qq=" + qq);
# 如果说订单订了多本书,那么将get到的这个json类型解析后得到订的所有书的相关信息之后插入数据库
def add_order(request):
    stu_id = request.session.get('studentID')
    name = request.GET.get('name')
    address = request.GET.get('address')
    zipcode = request.GET.get('zipcode')
    telephone = request.GET.get('telephone')
    qq = request.GET.get('qq')
    IsSured = request.GET.get("IsSured")
    order = watch_buy_models.Order()
    order.orderdate = timezone.now()
    order.user = login_manage_models.User.objects.get(studentID=stu_id)
    order.username = name
    order.address = address
    order.zipcode = zipcode
    order.telephone = telephone
    order.qq = qq
    order.IsHandled = IsSured
    order.save()
    jsonObj = request.GET.get('goods')
    if jsonObj is not None:
        good_dic = json.loads(jsonObj)
        count = 0
        while count < (len(good_dic) / 3):
            new_ordgood = watch_buy_models.OrderGood()
            new_ordgood.order = order
            new_ordgood.good = watch_buy_models.Goods.objects.get(GoodName=good_dic[("book_name" + str(count))])
            new_ordgood.save()
            count += 1
    else:
        ordergood = watch_buy_models.OrderGood()
        ordergood.order = order
        ordergood.save()
    return render(request, "watch_buy/add_order.html")


def delete_item(request):
    id = request.GET.get('id')
    cart_obj = watch_buy_models.Cart.objects.get(id=id)
    cart_obj.delete()
    return render(request, "watch_buy/delete_item.html", locals())


def changeqty(request):
    id = request.GET.get('id')
    qty = request.GET.get('qty')
    cart_obj = watch_buy_models.Cart.objects.get(id=id)
    cart_obj.Qty = qty
    cart_obj.save()
    return render(request, "watch_buy/changeqty.html", locals())


def delete_all(request):
    cart_obj = watch_buy_models.Cart.objects.all()
    cart_obj.delete()
    return render(request, "watch_buy/delete_all.html", locals())


def search(request):
    keyword = request.GET.get('search')
    rtn_set = set()
    rtn_list = []
    name_key = watch_buy_models.Goods.objects.filter(GoodName__contains=keyword)
    content_key = watch_buy_models.Goods.objects.filter(GoodIntro__contains=keyword)
    author_key = watch_buy_models.Goods.objects.filter(GoodAuthor__contains=keyword)
    ISBN_key = watch_buy_models.Goods.objects.filter(GoodISBN__contains=keyword)

    class Good:
        def __init__(self, good, pic, price):
            self.good = good
            self.pic = pic
            self.price = price

    for name in name_key:
        rtn_set.add(name)
    for content in content_key:
        rtn_set.add(content)
    for author in author_key:
        rtn_set.add(author)
    for ISBN in ISBN_key:
        rtn_set.add(ISBN)
    for rtn_good in rtn_set:
        rtn_list.append(Good(rtn_good, watch_buy_models.GoodsPic.objects.filter(GoodISBN_id=rtn_good.GoodISBN)[0], rtn_good.GoodPrice*rtn_good.GoodDiscount))
    return render(request, "watch_buy/search.html", locals())
